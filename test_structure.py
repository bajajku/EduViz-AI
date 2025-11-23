"""
Test script for the structured scene generation pipeline.
"""

import os
import sys
from data_processing.input_processor import InputProcessor
from data_processing.scene_parser import SceneParser


def test_text_processing():
    """Test text input processing with structured output."""
    print("=== Testing Text Input Processing ===")
    import dotenv
    dotenv.load_dotenv()
    # Create processor (you'll need to set GOOGLE_API_KEY env var)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Warning: GOOGLE_API_KEY not set. Cannot test actual API calls.")
        return
    
    processor = InputProcessor(api_key=api_key)
    
    # Test with mathematical content
    test_input = "(a+b)^2 = a^2 + 2ab + b^2"
    
    try:
        print(f"Processing input: {test_input}")
        scene_structure = processor.process_text_input(test_input)
        
        print("\n--- Generated Scene Structure ---")
        print(f"Title: {scene_structure.settings.title}")
        print(f"Description: {scene_structure.settings.description}")
        print(f"Duration: {scene_structure.settings.duration}s")
        print(f"Number of objects: {len(scene_structure.objects)}")
        print(f"Number of animations: {len(scene_structure.animations)}")
        
        print("\n--- Objects ---")
        for obj in scene_structure.objects:
            print(f"  {obj.id}: {obj.type.value} - '{obj.text_content}'")
        
        print("\n--- Animations ---")
        for anim in scene_structure.animations:
            print(f"  {anim.id}: {anim.type.value} -> {anim.target_objects}")
        
        print("\n--- Full JSON ---")
        print(scene_structure.to_json())
        
        return scene_structure
        
    except Exception as e:
        print(f"Error processing input: {e}")
        return None


def test_scene_parsing():
    """Test parsing structured scene for code generation."""
    print("\n=== Testing Scene Parsing ===")
    
    # First process some text
    scene_structure = test_text_processing()
    if not scene_structure:
        return
    
    # Parse for code generation
    parser = SceneParser()
    context = parser.parse(scene_structure)
    
    print("\n--- Code Generation Context ---")
    print(f"Scene Title: {context.scene_title}")
    print(f"Background Color: {context.background_color}")
    print(f"Total Duration: {context.total_duration}s")
    
    print(f"\nObject Counts:")
    print(f"  Text objects: {len(context.text_objects)}")
    print(f"  Shape objects: {len(context.shape_objects)}")
    print(f"  Math objects: {len(context.math_objects)}")
    print(f"  Line objects: {len(context.line_objects)}")
    print(f"  Graph objects: {len(context.graph_objects)}")
    
    print(f"\nAnimation Counts:")
    print(f"  Creation animations: {len(context.creation_animations)}")
    print(f"  Transformation animations: {len(context.transformation_animations)}")
    print(f"  Movement animations: {len(context.movement_animations)}")
    print(f"  Style animations: {len(context.style_animations)}")
    
    print(f"\nAnimation Timeline:")
    for start_time, anim in context.animation_timeline:
        print(f"  {start_time:4.1f}s: {anim.type.value} -> {anim.target_objects}")
    
    # Get imports needed
    imports = parser.get_imports_needed(context)
    print(f"\nImports needed:")
    for imp in imports:
        print(f"  {imp}")
    
    # Get creation order
    creation_order = parser.get_object_creation_order(context)
    print(f"\nObject creation order:")
    for i, obj in enumerate(creation_order):
        print(f"  {i+1}. {obj.id} ({obj.type.value})")
    
    # Get animation groups
    anim_groups = parser.get_animation_groups(context)
    print(f"\nAnimation groups (can play simultaneously):")
    for i, group in enumerate(anim_groups):
        print(f"  Group {i+1}: {[anim.id for anim in group]}")


def test_simple_example():
    """Test with a simple hardcoded example (no API required)."""
    print("\n=== Testing Simple Example (No API) ===")
    
    from data_processing.scene_structure import (
        SceneStructure, SceneObject, AnimationStep, ObjectType, AnimationType, 
        Position, Color, SceneSettings
    )
    
    # Create a simple scene manually
    settings = SceneSettings(
        title="Simple Circle Animation",
        description="A circle that appears and moves",
        duration=5.0,
        background_color=Color(name="BLACK")
    )
    
    objects = [
        SceneObject(
            id="circle1",
            type=ObjectType.CIRCLE,
            position=Position(-2, 0, 0),
            color=Color(name="BLUE"),
            size=1.0
        )
    ]
    
    animations = [
        AnimationStep(
            id="create_circle",
            type=AnimationType.CREATE,
            target_objects=["circle1"],
            duration=1.0,
            delay=0.0
        ),
        AnimationStep(
            id="move_circle",
            type=AnimationType.MOVE_TO,
            target_objects=["circle1"],
            duration=2.0,
            delay=1.0,
            target_position=Position(2, 0, 0)
        ),
        AnimationStep(
            id="fade_circle",
            type=AnimationType.FADE_OUT,
            target_objects=["circle1"],
            duration=1.0,
            delay=3.0
        )
    ]
    
    scene = SceneStructure(settings=settings, objects=objects, animations=animations)
    
    print("--- Manually Created Scene ---")
    print(scene.to_json())
    
    # Parse it
    parser = SceneParser()
    context = parser.parse(scene)
    
    print(f"\n--- Parsed Context ---")
    print(f"Title: {context.scene_title}")
    print(f"Shape objects: {len(context.shape_objects)}")
    print(f"Creation animations: {len(context.creation_animations)}")
    print(f"Movement animations: {len(context.movement_animations)}")
    print(f"Style animations: {len(context.style_animations)}")
    
    print(f"\nAnimation Timeline:")
    for start_time, anim in context.animation_timeline:
        print(f"  {start_time:4.1f}s: {anim.type.value} -> {anim.target_objects}")


if __name__ == "__main__":
    print("Testing Structured Scene Generation Pipeline")
    print("=" * 50)
    
    # Test simple example first (no API needed)
    # test_simple_example()
    
    # Test with real API (requires GOOGLE_API_KEY)
    test_text_processing()
    test_scene_parsing()
    
    print("\n" + "=" * 50)
    print("Testing complete!")
