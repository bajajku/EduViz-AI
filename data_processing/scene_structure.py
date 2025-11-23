"""
Scene Structure Definitions

Defines the standardized structure for scene descriptions that bridge
input processing and Manim code generation.
"""

from typing import List, Dict, Optional, Union, Literal
from dataclasses import dataclass, field
from enum import Enum
import json


class ObjectType(str, Enum):
    """Supported Manim object types."""
    TEXT = "text"
    CIRCLE = "circle"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    LINE = "line"
    ARROW = "arrow"
    POLYGON = "polygon"
    AXES = "axes"
    GRAPH = "graph"
    MATHTEXT = "mathtext"
    FORMULA = "formula"
    IMAGE = "image"
    GROUP = "group"


class AnimationType(str, Enum):
    """Supported Manim animation types."""
    CREATE = "create"
    WRITE = "write"
    DRAW_BORDER_THEN_FILL = "draw_border_then_fill"
    FADE_IN = "fade_in"
    FADE_OUT = "fade_out"
    TRANSFORM = "transform"
    REPLACE_TRANSFORM = "replace_transform"
    MOVE_TO = "move_to"
    SHIFT = "shift"
    ROTATE = "rotate"
    SCALE = "scale"
    SHOW_CREATION = "show_creation"
    UNCREATE = "uncreate"
    WIGGLE = "wiggle"
    INDICATE = "indicate"
    FLASH = "flash"
    CIRCUMSCRIBE = "circumscribe"


@dataclass
class Position:
    """3D position in Manim coordinate system."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    
    def to_list(self) -> List[float]:
        return [self.x, self.y, self.z]


@dataclass
class Color:
    """Color specification."""
    name: Optional[str] = None  # e.g., "BLUE", "RED"
    hex: Optional[str] = None   # e.g., "#FF0000"
    rgb: Optional[List[float]] = None  # e.g., [1.0, 0.0, 0.0]


@dataclass
class SceneObject:
    """Represents a single object in the scene."""
    id: str  # Unique identifier for the object
    type: ObjectType
    properties: Dict[str, Union[str, float, List[float], bool]] = field(default_factory=dict)
    position: Position = field(default_factory=Position)
    color: Optional[Color] = None
    text_content: Optional[str] = None  # For text/mathtext objects
    size: Optional[float] = None
    opacity: float = 1.0
    layer: int = 0  # Z-index for layering


@dataclass
class AnimationStep:
    """Represents a single animation step."""
    id: str  # Unique identifier for the animation
    type: AnimationType
    target_objects: List[str]  # List of object IDs to animate
    duration: float = 1.0  # Duration in seconds
    delay: float = 0.0  # Delay before starting animation
    properties: Dict[str, Union[str, float, List[float], bool]] = field(default_factory=dict)
    easing: str = "smooth"  # Easing function name
    
    # For transform animations
    from_object: Optional[str] = None
    to_object: Optional[str] = None
    
    # For movement animations
    target_position: Optional[Position] = None
    offset: Optional[Position] = None


@dataclass
class SceneSettings:
    """Overall scene configuration."""
    title: str = ""
    description: str = ""
    duration: float = 10.0  # Total scene duration in seconds
    background_color: Color = field(default_factory=lambda: Color(name="BLACK"))
    camera_position: Position = field(default_factory=Position)
    quality: str = "medium_quality"  # low_quality, medium_quality, high_quality
    resolution: str = "720p"  # 480p, 720p, 1080p, 4k


@dataclass
class SceneStructure:
    """Complete structured scene description."""
    settings: SceneSettings = field(default_factory=SceneSettings)
    objects: List[SceneObject] = field(default_factory=list)
    animations: List[AnimationStep] = field(default_factory=list)
    
    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2, default=str)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "settings": {
                "title": self.settings.title,
                "description": self.settings.description,
                "duration": self.settings.duration,
                "background_color": {
                    "name": self.settings.background_color.name,
                    "hex": self.settings.background_color.hex,
                    "rgb": self.settings.background_color.rgb
                },
                "camera_position": self.settings.camera_position.to_list(),
                "quality": self.settings.quality,
                "resolution": self.settings.resolution
            },
            "objects": [
                {
                    "id": obj.id,
                    "type": obj.type.value,
                    "properties": obj.properties,
                    "position": obj.position.to_list(),
                    "color": {
                        "name": obj.color.name if obj.color else None,
                        "hex": obj.color.hex if obj.color else None,
                        "rgb": obj.color.rgb if obj.color else None
                    } if obj.color else None,
                    "text_content": obj.text_content,
                    "size": obj.size,
                    "opacity": obj.opacity,
                    "layer": obj.layer
                }
                for obj in self.objects
            ],
            "animations": [
                {
                    "id": anim.id,
                    "type": anim.type.value,
                    "target_objects": anim.target_objects,
                    "duration": anim.duration,
                    "delay": anim.delay,
                    "properties": anim.properties,
                    "easing": anim.easing,
                    "from_object": anim.from_object,
                    "to_object": anim.to_object,
                    "target_position": anim.target_position.to_list() if anim.target_position else None,
                    "offset": anim.offset.to_list() if anim.offset else None
                }
                for anim in self.animations
            ]
        }
    
    @classmethod
    def from_json(cls, json_str: str) -> 'SceneStructure':
        """Create SceneStructure from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SceneStructure':
        """Create SceneStructure from dictionary."""
        # Parse settings
        settings_data = data.get("settings", {})
        bg_color_data = settings_data.get("background_color", {})
        bg_color = Color(
            name=bg_color_data.get("name"),
            hex=bg_color_data.get("hex"),
            rgb=bg_color_data.get("rgb")
        )
        cam_pos = settings_data.get("camera_position", [0, 0, 0])
        camera_position = Position(cam_pos[0], cam_pos[1], cam_pos[2])
        
        settings = SceneSettings(
            title=settings_data.get("title", ""),
            description=settings_data.get("description", ""),
            duration=settings_data.get("duration", 10.0),
            background_color=bg_color,
            camera_position=camera_position,
            quality=settings_data.get("quality", "medium_quality"),
            resolution=settings_data.get("resolution", "720p")
        )
        
        # Parse objects
        objects = []
        for obj_data in data.get("objects", []):
            pos_data = obj_data.get("position", [0, 0, 0])
            position = Position(pos_data[0], pos_data[1], pos_data[2])
            
            color = None
            color_data = obj_data.get("color")
            if color_data:
                color = Color(
                    name=color_data.get("name"),
                    hex=color_data.get("hex"),
                    rgb=color_data.get("rgb")
                )
            
            obj = SceneObject(
                id=obj_data["id"],
                type=ObjectType(obj_data["type"]),
                properties=obj_data.get("properties", {}),
                position=position,
                color=color,
                text_content=obj_data.get("text_content"),
                size=obj_data.get("size"),
                opacity=obj_data.get("opacity", 1.0),
                layer=obj_data.get("layer", 0)
            )
            objects.append(obj)
        
        # Parse animations
        animations = []
        for anim_data in data.get("animations", []):
            target_pos = None
            if anim_data.get("target_position"):
                pos_data = anim_data["target_position"]
                target_pos = Position(pos_data[0], pos_data[1], pos_data[2])
            
            offset = None
            if anim_data.get("offset"):
                offset_data = anim_data["offset"]
                offset = Position(offset_data[0], offset_data[1], offset_data[2])
            
            anim = AnimationStep(
                id=anim_data["id"],
                type=AnimationType(anim_data["type"]),
                target_objects=anim_data["target_objects"],
                duration=anim_data.get("duration", 1.0),
                delay=anim_data.get("delay", 0.0),
                properties=anim_data.get("properties", {}),
                easing=anim_data.get("easing", "smooth"),
                from_object=anim_data.get("from_object"),
                to_object=anim_data.get("to_object"),
                target_position=target_pos,
                offset=offset
            )
            animations.append(anim)
        
        return cls(settings=settings, objects=objects, animations=animations)


# JSON Schema for validation
SCENE_STRUCTURE_SCHEMA = {
    "type": "object",
    "required": ["settings", "objects", "animations"],
    "properties": {
        "settings": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "duration": {"type": "number", "minimum": 0},
                "background_color": {
                    "type": "object",
                    "properties": {
                        "name": {"type": ["string", "null"]},
                        "hex": {"type": ["string", "null"]},
                        "rgb": {"type": ["array", "null"], "items": {"type": "number"}}
                    }
                },
                "camera_position": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                "quality": {"type": "string", "enum": ["low_quality", "medium_quality", "high_quality"]},
                "resolution": {"type": "string", "enum": ["480p", "720p", "1080p", "4k"]}
            }
        },
        "objects": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "type"],
                "properties": {
                    "id": {"type": "string"},
                    "type": {"type": "string", "enum": [e.value for e in ObjectType]},
                    "properties": {"type": "object"},
                    "position": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
                    "color": {
                        "type": ["object", "null"],
                        "properties": {
                            "name": {"type": ["string", "null"]},
                            "hex": {"type": ["string", "null"]},
                            "rgb": {"type": ["array", "null"]}
                        }
                    },
                    "text_content": {"type": ["string", "null"]},
                    "size": {"type": ["number", "null"]},
                    "opacity": {"type": "number", "minimum": 0, "maximum": 1},
                    "layer": {"type": "integer"}
                }
            }
        },
        "animations": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "type", "target_objects"],
                "properties": {
                    "id": {"type": "string"},
                    "type": {"type": "string", "enum": [e.value for e in AnimationType]},
                    "target_objects": {"type": "array", "items": {"type": "string"}},
                    "duration": {"type": "number", "minimum": 0},
                    "delay": {"type": "number", "minimum": 0},
                    "properties": {"type": "object"},
                    "easing": {"type": "string"},
                    "from_object": {"type": ["string", "null"]},
                    "to_object": {"type": ["string", "null"]},
                    "target_position": {"type": ["array", "null"], "items": {"type": "number"}},
                    "offset": {"type": ["array", "null"], "items": {"type": "number"}}
                }
            }
        }
    }
}
