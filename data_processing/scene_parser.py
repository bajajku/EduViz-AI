"""
Scene Parser Module

Parses structured scene descriptions and extracts information needed for
Manim code generation. Provides convenient methods to access scene elements
in a format optimized for code generation.
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from .scene_structure import SceneStructure, SceneObject, AnimationStep, ObjectType, AnimationType


@dataclass 
class CodeGenerationContext:
    """Context object containing parsed scene information for code generation."""
    
    # Scene metadata
    scene_title: str
    scene_description: str
    total_duration: float
    background_color: str
    
    # Objects grouped by type for easier code generation
    text_objects: List[SceneObject]
    shape_objects: List[SceneObject]  # circles, squares, rectangles, etc.
    math_objects: List[SceneObject]   # formulas, mathtext
    line_objects: List[SceneObject]   # lines, arrows
    graph_objects: List[SceneObject]  # axes, graphs
    
    # Animations grouped by type and sorted by timing
    creation_animations: List[AnimationStep]
    transformation_animations: List[AnimationStep]
    movement_animations: List[AnimationStep]
    style_animations: List[AnimationStep]  # fade, scale, etc.
    
    # Timing information
    animation_timeline: List[Tuple[float, AnimationStep]]  # (start_time, animation)
    
    # Object dependencies and relationships
    object_dependencies: Dict[str, List[str]]  # object_id -> [dependent_object_ids]
    transformation_chains: List[List[str]]     # chains of object transformations


class SceneParser:
    """Parses SceneStructure objects for code generation."""
    
    def __init__(self):
        """Initialize the parser."""
        pass
    
    def parse(self, scene: SceneStructure) -> CodeGenerationContext:
        """
        Parse a SceneStructure into a CodeGenerationContext.
        
        Args:
            scene: SceneStructure object to parse
            
        Returns:
            CodeGenerationContext with organized data for code generation
        """
        # Extract scene metadata
        scene_title = scene.settings.title or "Generated Scene"
        scene_description = scene.settings.description or ""
        total_duration = scene.settings.duration
        background_color = self._parse_color(scene.settings.background_color)
        
        # Group objects by type
        text_objects = []
        shape_objects = []
        math_objects = []
        line_objects = []
        graph_objects = []
        
        for obj in scene.objects:
            if obj.type in [ObjectType.TEXT]:
                text_objects.append(obj)
            elif obj.type in [ObjectType.MATHTEXT, ObjectType.FORMULA]:
                math_objects.append(obj)
            elif obj.type in [ObjectType.CIRCLE, ObjectType.SQUARE, ObjectType.RECTANGLE, ObjectType.POLYGON]:
                shape_objects.append(obj)
            elif obj.type in [ObjectType.LINE, ObjectType.ARROW]:
                line_objects.append(obj)
            elif obj.type in [ObjectType.AXES, ObjectType.GRAPH]:
                graph_objects.append(obj)
        
        # Group animations by type
        creation_animations = []
        transformation_animations = []
        movement_animations = []
        style_animations = []
        
        for anim in scene.animations:
            if anim.type in [AnimationType.CREATE, AnimationType.WRITE, AnimationType.SHOW_CREATION, AnimationType.DRAW_BORDER_THEN_FILL]:
                creation_animations.append(anim)
            elif anim.type in [AnimationType.TRANSFORM, AnimationType.REPLACE_TRANSFORM]:
                transformation_animations.append(anim)
            elif anim.type in [AnimationType.MOVE_TO, AnimationType.SHIFT]:
                movement_animations.append(anim)
            elif anim.type in [AnimationType.FADE_IN, AnimationType.FADE_OUT, AnimationType.SCALE, AnimationType.ROTATE, AnimationType.WIGGLE, AnimationType.INDICATE, AnimationType.FLASH, AnimationType.CIRCUMSCRIBE]:
                style_animations.append(anim)
        
        # Create animation timeline
        animation_timeline = []
        for anim in scene.animations:
            start_time = anim.delay
            animation_timeline.append((start_time, anim))
        animation_timeline.sort(key=lambda x: x[0])  # Sort by start time
        
        # Analyze object dependencies and transformation chains
        object_dependencies = self._analyze_dependencies(scene)
        transformation_chains = self._find_transformation_chains(scene)
        
        return CodeGenerationContext(
            scene_title=scene_title,
            scene_description=scene_description,
            total_duration=total_duration,
            background_color=background_color,
            text_objects=text_objects,
            shape_objects=shape_objects,
            math_objects=math_objects,
            line_objects=line_objects,
            graph_objects=graph_objects,
            creation_animations=creation_animations,
            transformation_animations=transformation_animations,
            movement_animations=movement_animations,
            style_animations=style_animations,
            animation_timeline=animation_timeline,
            object_dependencies=object_dependencies,
            transformation_chains=transformation_chains
        )
    
    def get_imports_needed(self, context: CodeGenerationContext) -> List[str]:
        """
        Determine which Manim imports are needed based on the scene content.
        
        Args:
            context: Parsed scene context
            
        Returns:
            List of import statements needed
        """
        imports = ["from manim import *"]
        
        # Check if we need additional imports based on object types
        if context.math_objects:
            imports.append("import numpy as np")
        
        if context.graph_objects:
            imports.append("import numpy as np")
        
        return imports
    
    def get_object_creation_order(self, context: CodeGenerationContext) -> List[SceneObject]:
        """
        Get the optimal order for creating objects based on dependencies.
        
        Args:
            context: Parsed scene context
            
        Returns:
            List of objects in creation order
        """
        # Simple topological sort based on dependencies
        all_objects = (context.text_objects + context.shape_objects + 
                      context.math_objects + context.line_objects + context.graph_objects)
        
        # For now, return objects sorted by layer then by creation time
        # In the future, this could implement proper dependency resolution
        return sorted(all_objects, key=lambda obj: (obj.layer, obj.id))
    
    def get_animation_groups(self, context: CodeGenerationContext) -> List[List[AnimationStep]]:
        """
        Group animations that can be played simultaneously.
        
        Args:
            context: Parsed scene context
            
        Returns:
            List of animation groups (each group can be played together)
        """
        # Group animations by their start time (delay)
        time_groups = {}
        for anim in context.creation_animations + context.transformation_animations + context.movement_animations + context.style_animations:
            start_time = anim.delay
            if start_time not in time_groups:
                time_groups[start_time] = []
            time_groups[start_time].append(anim)
        
        # Return groups sorted by time
        return [time_groups[time] for time in sorted(time_groups.keys())]
    
    def _parse_color(self, color) -> str:
        """Parse color object to Manim color string."""
        if color and color.name:
            return color.name
        elif color and color.hex:
            return f'"{color.hex}"'
        elif color and color.rgb:
            return f"rgb_to_color({color.rgb})"
        else:
            return "WHITE"
    
    def _analyze_dependencies(self, scene: SceneStructure) -> Dict[str, List[str]]:
        """Analyze object dependencies based on animations."""
        dependencies = {obj.id: [] for obj in scene.objects}
        
        # Find dependencies from transformation animations
        for anim in scene.animations:
            if anim.type in [AnimationType.TRANSFORM, AnimationType.REPLACE_TRANSFORM]:
                if anim.from_object and anim.to_object:
                    # to_object depends on from_object
                    if anim.to_object not in dependencies:
                        dependencies[anim.to_object] = []
                    dependencies[anim.to_object].append(anim.from_object)
        
        return dependencies
    
    def _find_transformation_chains(self, scene: SceneStructure) -> List[List[str]]:
        """Find chains of object transformations."""
        chains = []
        
        # Track transformation relationships
        transform_map = {}
        for anim in scene.animations:
            if anim.type in [AnimationType.TRANSFORM, AnimationType.REPLACE_TRANSFORM]:
                if anim.from_object and anim.to_object:
                    transform_map[anim.from_object] = anim.to_object
        
        # Find chains
        visited = set()
        for obj_id in transform_map:
            if obj_id not in visited:
                chain = []
                current = obj_id
                while current and current not in visited:
                    chain.append(current)
                    visited.add(current)
                    current = transform_map.get(current)
                
                if len(chain) > 1:
                    chains.append(chain)
        
        return chains


def parse_scene(scene: SceneStructure) -> CodeGenerationContext:
    """
    Convenience function to parse a scene.
    
    Args:
        scene: SceneStructure to parse
        
    Returns:
        CodeGenerationContext for code generation
    """
    parser = SceneParser()
    return parser.parse(scene)


# Example usage and testing
if __name__ == "__main__":
    from .scene_structure import SceneStructure, SceneObject, AnimationStep, ObjectType, AnimationType, Position, Color, SceneSettings
    
    # Create a sample scene
    settings = SceneSettings(
        title="Sample Math Scene",
        description="Shows algebraic expansion",
        duration=8.0
    )
    
    objects = [
        SceneObject(
            id="formula1",
            type=ObjectType.MATHTEXT,
            text_content="(a+b)^2",
            position=Position(-2, 0, 0),
            color=Color(name="BLUE")
        ),
        SceneObject(
            id="formula2", 
            type=ObjectType.MATHTEXT,
            text_content="a^2 + 2ab + b^2",
            position=Position(2, 0, 0),
            color=Color(name="GREEN")
        )
    ]
    
    animations = [
        AnimationStep(
            id="create_formula1",
            type=AnimationType.WRITE,
            target_objects=["formula1"],
            duration=2.0,
            delay=0.0
        ),
        AnimationStep(
            id="transform_formula",
            type=AnimationType.TRANSFORM,
            target_objects=["formula1"],
            from_object="formula1",
            to_object="formula2",
            duration=3.0,
            delay=2.0
        )
    ]
    
    scene = SceneStructure(settings=settings, objects=objects, animations=animations)
    
    # Parse the scene
    context = parse_scene(scene)
    
    print("Parsed Scene Context:")
    print(f"Title: {context.scene_title}")
    print(f"Math objects: {len(context.math_objects)}")
    print(f"Creation animations: {len(context.creation_animations)}")
    print(f"Transformation animations: {len(context.transformation_animations)}")
    print(f"Animation timeline: {context.animation_timeline}")
