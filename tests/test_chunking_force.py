"""
Test multi-scene processing with content that forces multiple chunks.
"""

import os
import sys
from pathlib import Path

try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from data_processing.multi_scene_processor import MultiSceneProcessor


def test_forced_chunking():
    """Test with content long enough to force multiple chunks."""
    print("=== Testing Forced Multi-Chunk Processing ===")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not set")
        return False
    
    # Create content with clear sections that should be chunked
    long_content = """
    Physics Fundamentals Course
    
    Unit 1: Classical Mechanics
    Classical mechanics describes the motion of objects from projectiles to parts of machinery, and astronomical objects like spacecraft, planets, stars, and galaxies. Newton's laws of motion form the foundation of classical mechanics. The first law states that an object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force. The second law defines force as F = ma, where force equals mass times acceleration. The third law states that for every action, there is an equal and opposite reaction.
    
    Unit 2: Thermodynamics  
    Thermodynamics is the branch of physics that deals with heat and temperature, and their relation to energy, work, radiation, and properties of matter. The first law of thermodynamics states that energy cannot be created or destroyed, only transferred or changed from one form to another. This is also known as the conservation of energy. The second law introduces the concept of entropy, stating that the entropy of an isolated system never decreases. Heat flows naturally from hot to cold objects, and it takes work to move heat from cold to hot.
    
    Unit 3: Electromagnetism
    Electromagnetism is a branch of physics involving the study of the electromagnetic force, a type of physical interaction that occurs between electrically charged particles. The electromagnetic force is carried by electromagnetic fields composed of electric fields and magnetic fields, and it is responsible for electromagnetic radiation such as light. Electric fields are created by electric charges, while magnetic fields are created by moving charges (electric currents). Maxwell's equations describe how electric and magnetic fields are generated and altered by each other and by charges and currents.
    
    Unit 4: Quantum Mechanics
    Quantum mechanics is a fundamental theory in physics that provides a description of the physical properties of nature at the scale of atoms and subatomic particles. It explains phenomena that classical physics cannot, such as wave-particle duality and quantum entanglement. The uncertainty principle, formulated by Werner Heisenberg, states that the more precisely the position of a particle is determined, the less precisely its momentum can be known, and vice versa. Schrödinger's equation is the fundamental equation of quantum mechanics that describes how the quantum state of a physical system changes over time.
    """
    
    try:
        processor = MultiSceneProcessor(api_key=api_key)
        
        print(f"Processing document with {len(long_content)} characters...")
        
        multi_scene = processor.process_combined_input(
            text_input=long_content,
            document_title="Physics Fundamentals",
        )
        
        print(f"✓ Successfully created multi-scene video!")
        print(f"  Title: {multi_scene.title}")
        print(f"  Number of scenes: {len(multi_scene.scenes)}")
        print(f"  Total duration: {multi_scene.total_duration:.1f} seconds")
        
        print(f"\nScene breakdown:")
        for i, scene in enumerate(multi_scene.scenes):
            print(f"  Scene {i+1}: {scene.settings.title}")
            print(f"    Duration: {scene.settings.duration:.1f}s")
            print(f"    Objects: {len(scene.objects)}")
            print(f"    Animations: {len(scene.animations)}")
        
        # Generate the combined code
        print(f"\nGenerating combined Manim code...")
        combined_code = processor.generate_combined_code(multi_scene)
        
        print(f"✓ Generated code with {len(combined_code)} characters")
        
        # Save the code
        with open("physics_multi_scene.py", "w") as f:
            f.write(combined_code)
        print("✓ Saved to physics_multi_scene.py")
        
        # Show some stats
        print(f"\nStatistics:")
        print(f"  Average scene duration: {multi_scene.total_duration / len(multi_scene.scenes):.1f}s")
        print(f"  Scenes per minute: {len(multi_scene.scenes) / (multi_scene.total_duration / 60):.1f}")
        
        return True
        
    except Exception as e:
        print(f"✗ Failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_forced_chunking()
    if success:
        print("\n🎉 Multi-scene processing working perfectly!")
    else:
        print("\n❌ Multi-scene processing needs debugging.")


