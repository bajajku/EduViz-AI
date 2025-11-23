from manim import *
import numpy as np

class CombinedVideo(Scene):
    """
    Calculus Reference Guide
    Multi-scene video with 1 parts
    
    Total Duration: 45.0 seconds
    Number of Scenes: 1
    """
    
    def construct(self):
        """Main video construction with multiple scenes."""
        # Title card
        title = Text("Calculus Reference Guide", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Play all scenes in sequence
        self.scene_1()
        
        # End card
        end_text = Text("End", font_size=36)
        self.play(FadeIn(end_text))
        self.wait(1)

    def scene_1(self):
        """Scene 1: Calculus Reference Guide - Part 1"""
        # Clear previous scene
        self.clear()
        
        # Scene content
        self.camera.background_color = BLACK

        # Create objects
        mobjects = {}

        # main_title
        mobjects["main_title"] = Text("Calculus Quick Reference", font_size=1.2, color=WHITE)
        mobjects["main_title"].move_to([0, 3.5, 0])
        mobjects["main_title"].set_opacity(1.0)

        # deriv_section_title
        mobjects["deriv_section_title"] = Text("Derivatives:", font_size=0.9, color=YELLOW)
        mobjects["deriv_section_title"].move_to([-5.5, 2.5, 0])
        mobjects["deriv_section_title"].set_opacity(1.0)

        # deriv_def
        mobjects["deriv_def"] = Text("The derivative of f(x) represents the instantaneous rate of change.", font_size=0.7, color=WHITE)
        mobjects["deriv_def"].move_to([0, 1.8, 0])
        mobjects["deriv_def"].set_opacity(1.0)

        # deriv_basic_rules_title
        mobjects["deriv_basic_rules_title"] = Text("Basic Rules:", font_size=0.8, color=GREEN)
        mobjects["deriv_basic_rules_title"].move_to([-5.5, 0.8, 0])
        mobjects["deriv_basic_rules_title"].set_opacity(1.0)

        # deriv_rule_power_name (Adjusted opacity to 0.0 for FadeIn animation)
        mobjects["deriv_rule_power_name"] = Text("(Power Rule)", font_size=0.6, color=GRAY)
        mobjects["deriv_rule_power_name"].move_to([2.5, 0.2, 0])
        mobjects["deriv_rule_power_name"].set_opacity(0.0) 

        # deriv_product_rule_title
        mobjects["deriv_product_rule_title"] = Text("Product Rule:", font_size=0.8, color=GREEN)
        mobjects["deriv_product_rule_title"].move_to([-5.5, -2.8, 0])
        mobjects["deriv_product_rule_title"].set_opacity(1.0)

        # deriv_chain_rule_title
        mobjects["deriv_chain_rule_title"] = Text("Chain Rule:", font_size=0.8, color=GREEN)
        mobjects["deriv_chain_rule_title"].move_to([-5.5, -3.5, 0])
        mobjects["deriv_chain_rule_title"].set_opacity(1.0)

        # integral_section_title
        mobjects["integral_section_title"] = Text("Integrals:", font_size=0.9, color=YELLOW)
        mobjects["integral_section_title"].move_to([-5.5, 2.5, 0])
        mobjects["integral_section_title"].set_opacity(0.0)

        # integral_def
        mobjects["integral_def"] = Text("Integration is the reverse of differentiation.", font_size=0.7, color=WHITE)
        mobjects["integral_def"].move_to([0, 1.8, 0])
        mobjects["integral_def"].set_opacity(0.0)

        # integral_basic_rules_title
        mobjects["integral_basic_rules_title"] = Text("Basic Rules:", font_size=0.8, color=GREEN)
        mobjects["integral_basic_rules_title"].move_to([-5.5, 0.8, 0])
        mobjects["integral_basic_rules_title"].set_opacity(0.0)

        # ftc_title
        mobjects["ftc_title"] = Text("Fundamental Theorem of Calculus:", font_size=0.8, color=GREEN)
        mobjects["ftc_title"].move_to([-5.5, -2.8, 0])
        mobjects["ftc_title"].set_opacity(0.0)

        # applications_title
        mobjects["applications_title"] = Text("Applications:", font_size=0.9, color=YELLOW)
        mobjects["applications_title"].move_to([-5.5, 2.5, 0])
        mobjects["applications_title"].set_opacity(0.0)

        # applications_text
        mobjects["applications_text"] = Text("Calculus is used in physics for motion, in economics for optimization, and in engineering for system analysis.", font_size=0.7, color=WHITE)
        mobjects["applications_text"].move_to([0, 1.8, 0])
        mobjects["applications_text"].set_opacity(0.0)

        # deriv_rule_power_form
        mobjects["deriv_rule_power_form"] = MathTex(r"\frac{d}{dx}[x^n] = nx^{n-1}", font_size=0.7, color=WHITE)
        mobjects["deriv_rule_power_form"].move_to([-1.5, 0.2, 0])
        mobjects["deriv_rule_power_form"].set_opacity(1.0)

        # deriv_rule_sin_form
        mobjects["deriv_rule_sin_form"] = MathTex(r"\frac{d}{dx}[\sin(x)] = \cos(x)", font_size=0.7, color=WHITE)
        mobjects["deriv_rule_sin_form"].move_to([-1.5, -0.3, 0])
        mobjects["deriv_rule_sin_form"].set_opacity(1.0)

        # deriv_rule_cos_form
        mobjects["deriv_rule_cos_form"] = MathTex(r"\frac{d}{dx}[\cos(x)] = -\sin(x)", font_size=0.7, color=WHITE)
        mobjects["deriv_rule_cos_form"].move_to([-1.5, -0.8, 0])
        mobjects["deriv_rule_cos_form"].set_opacity(1.0)

        # deriv_rule_exp_form
        mobjects["deriv_rule_exp_form"] = MathTex(r"\frac{d}{dx}[e^x] = e^x", font_size=0.7, color=WHITE)
        mobjects["deriv_rule_exp_form"].move_to([-1.5, -1.3, 0])
        mobjects["deriv_rule_exp_form"].set_opacity(1.0)

        # deriv_rule_ln_form
        mobjects["deriv_rule_ln_form"] = MathTex(r"\frac{d}{dx}[\ln(x)] = \frac{1}{x}", font_size=0.7, color=WHITE)
        mobjects["deriv_rule_ln_form"].move_to([-1.5, -1.8, 0])
        mobjects["deriv_rule_ln_form"].set_opacity(1.0)

        # deriv_product_rule_form
        mobjects["deriv_product_rule_form"] = MathTex(r"\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)", font_size=0.7, color=WHITE)
        mobjects["deriv_product_rule_form"].move_to([0.5, -2.8, 0])
        mobjects["deriv_product_rule_form"].set_opacity(1.0)

        # deriv_chain_rule_form
        mobjects["deriv_chain_rule_form"] = MathTex(r"\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x)", font_size=0.7, color=WHITE)
        mobjects["deriv_chain_rule_form"].move_to([0.5, -3.5, 0])
        mobjects["deriv_chain_rule_form"].set_opacity(1.0)

        # integral_rule_power_form
        mobjects["integral_rule_power_form"] = MathTex(r"\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)", font_size=0.7, color=WHITE)
        mobjects["integral_rule_power_form"].move_to([-1.5, 0.2, 0])
        mobjects["integral_rule_power_form"].set_opacity(0.0)

        # integral_rule_sin_form
        mobjects["integral_rule_sin_form"] = MathTex(r"\int \sin(x) dx = -\cos(x) + C", font_size=0.7, color=WHITE)
        mobjects["integral_rule_sin_form"].move_to([-1.5, -0.3, 0])
        mobjects["integral_rule_sin_form"].set_opacity(0.0)

        # integral_rule_cos_form
        mobjects["integral_rule_cos_form"] = MathTex(r"\int \cos(x) dx = \sin(x) + C", font_size=0.7, color=WHITE)
        mobjects["integral_rule_cos_form"].move_to([-1.5, -0.8, 0])
        mobjects["integral_rule_cos_form"].set_opacity(0.0)

        # integral_rule_exp_form
        mobjects["integral_rule_exp_form"] = MathTex(r"\int e^x dx = e^x + C", font_size=0.7, color=WHITE)
        mobjects["integral_rule_exp_form"].move_to([-1.5, -1.3, 0])
        mobjects["integral_rule_exp_form"].set_opacity(0.0)

        # integral_rule_ln_form
        mobjects["integral_rule_ln_form"] = MathTex(r"\int \frac{1}{x} dx = \ln|x| + C", font_size=0.7, color=WHITE)
        mobjects["integral_rule_ln_form"].move_to([-1.5, -1.8, 0])
        mobjects["integral_rule_ln_form"].set_opacity(0.0)

        # ftc_form
        mobjects["ftc_form"] = MathTex(r"\text{If } F(x) = \int_{a}^{x} f(t) dt, \text{ then } F'(x) = f(x)", font_size=0.7, color=WHITE)
        mobjects["ftc_form"].move_to([0.5, -2.8, 0])
        mobjects["ftc_form"].set_opacity(0.0)

        # Animation Timeline
        current_time = 0.0
        scene_total_duration = 45.0

        animations_data = [
            {"start_time": 0.0, "animation_id": "anim_deriv_rule_power_name", "animation_type": "fade_in", "targets": ["deriv_rule_power_name"], "duration": 0.5},
            {"start_time": 0.0, "animation_id": "anim_deriv_product_rule_form", "animation_type": "write", "targets": ["deriv_product_rule_form"], "duration": 2.0},
            {"start_time": 0.0, "animation_id": "anim_deriv_chain_rule_form", "animation_type": "write", "targets": ["deriv_chain_rule_form"], "duration": 2.0},
            {"start_time": 0.0, "animation_id": "anim_ftc_form", "animation_type": "fade_in", "targets": ["ftc_form"], "duration": 2.0},
            {"start_time": 0.3, "animation_id": "anim_deriv_rule_power", "animation_type": "write", "targets": ["deriv_rule_power_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_deriv_rule_sin", "animation_type": "write", "targets": ["deriv_rule_sin_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_deriv_rule_cos", "animation_type": "write", "targets": ["deriv_rule_cos_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_deriv_rule_exp", "animation_type": "write", "targets": ["deriv_rule_exp_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_deriv_rule_ln", "animation_type": "write", "targets": ["deriv_rule_ln_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_integral_rule_power", "animation_type": "fade_in", "targets": ["integral_rule_power_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_integral_rule_sin", "animation_type": "fade_in", "targets": ["integral_rule_sin_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_integral_rule_cos", "animation_type": "fade_in", "targets": ["integral_rule_cos_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_integral_rule_exp", "animation_type": "fade_in", "targets": ["integral_rule_exp_form"], "duration": 1.5},
            {"start_time": 0.3, "animation_id": "anim_integral_rule_ln", "animation_type": "fade_in", "targets": ["integral_rule_ln_form"], "duration": 1.5},
            {"start_time": 0.5, "animation_id": "anim_main_title", "animation_type": "write", "targets": ["main_title"], "duration": 1.5},
            {"start_time": 0.5, "animation_id": "anim_deriv_def", "animation_type": "write", "targets": ["deriv_def"], "duration": 2.0},
            {"start_time": 0.5, "animation_id": "anim_deriv_basic_rules_title", "animation_type": "write", "targets": ["deriv_basic_rules_title"], "duration": 1.0},
            {"start_time": 0.5, "animation_id": "anim_integral_section_title", "animation_type": "fade_in", "targets": ["integral_section_title"], "duration": 1.0},
            {"start_time": 0.5, "animation_id": "anim_integral_def", "animation_type": "fade_in", "targets": ["integral_def"], "duration": 2.0},
            {"start_time": 0.5, "animation_id": "anim_integral_basic_rules_title", "animation_type": "fade_in", "targets": ["integral_basic_rules_title"], "duration": 1.0},
            {"start_time": 0.5, "animation_id": "anim_applications_title", "animation_type": "fade_in", "targets": ["applications_title"], "duration": 1.0},
            {"start_time": 0.5, "animation_id": "anim_applications_text", "animation_type": "fade_in", "targets": ["applications_text"], "duration": 3.0},
            {"start_time": 0.8, "animation_id": "anim_deriv_product_rule_title", "animation_type": "write", "targets": ["deriv_product_rule_title"], "duration": 1.0},
            {"start_time": 0.8, "animation_id": "anim_deriv_chain_rule_title", "animation_type": "write", "targets": ["deriv_chain_rule_title"], "duration": 1.0},
            {"start_time": 0.8, "animation_id": "anim_ftc_title", "animation_type": "fade_in", "targets": ["ftc_title"], "duration": 1.0},
            {"start_time": 1.0, "animation_id": "anim_deriv_section_title", "animation_type": "write", "targets": ["deriv_section_title"], "duration": 1.0},
            {"start_time": 1.0, "animation_id": "anim_fade_out_deriv_section", "animation_type": "fade_out", "targets": ["deriv_section_title", "deriv_def", "deriv_basic_rules_title", "deriv_rule_power_form", "deriv_rule_power_name", "deriv_rule_sin_form", "deriv_rule_cos_form", "deriv_rule_exp_form", "deriv_rule_ln_form", "deriv_product_rule_title", "deriv_product_rule_form", "deriv_chain_rule_title", "deriv_chain_rule_form"], "duration": 1.0},
            {"start_time": 1.0, "animation_id": "anim_fade_out_integral_section", "animation_type": "fade_out", "targets": ["integral_section_title", "integral_def", "integral_basic_rules_title", "integral_rule_power_form", "integral_rule_sin_form", "integral_rule_cos_form", "integral_rule_exp_form", "integral_rule_ln_form", "ftc_title", "ftc_form"], "duration": 1.0},
            {"start_time": 2.0, "animation_id": "anim_fade_out_all", "animation_type": "fade_out", "targets": ["main_title", "applications_title", "applications_text"], "duration": 1.5}
        ]

        # Sort animations by start_time to ensure correct chronological order
        animations_data.sort(key=lambda x: x["start_time"])

        # Group animations that start at the same time
        grouped_animations = {}
        for anim in animations_data:
            start_time = anim["start_time"]
            if start_time not in grouped_animations:
                grouped_animations[start_time] = []
            grouped_animations[start_time].append(anim)

        sorted_start_times = sorted(grouped_animations.keys())

        for start_time in sorted_start_times:
            # Wait for the next animation block
            if start_time > current_time:
                self.wait(start_time - current_time)
            current_time = start_time # Update current_time to the start of the current block

            animations_to_play = []
            max_duration_in_group = 0.0

            for anim in grouped_animations[start_time]:
                target_mobjects = [mobjects[obj_id] for obj_id in anim["targets"]]
                duration = anim["duration"]
                max_duration_in_group = max(max_duration_in_group, duration)

                # Use VGroup to treat multiple targets as a single Mobject for animations
                if anim["animation_type"] == "write":
                    animations_to_play.append(Write(VGroup(*target_mobjects)))
                elif anim["animation_type"] == "create":
                    animations_to_play.append(Create(VGroup(*target_mobjects)))
                elif anim["animation_type"] == "fade_in":
                    animations_to_play.append(FadeIn(VGroup(*target_mobjects)))
                elif anim["animation_type"] == "fade_out":
                    animations_to_play.append(FadeOut(VGroup(*target_mobjects)))
                # Add other animation types if they were present in the data
                # elif anim["animation_type"] == "transform":
                #     animations_to_play.append(Transform(mobjects[anim["from_object"]], mobjects[anim["to_object"]]))
                # elif anim["animation_type"] == "move_to":
                #     animations_to_play.append(mobjects[anim["target_objects"][0]].animate.move_to(anim["target_position"]))
                else:
                    print(f"Warning: Unknown animation type {anim['animation_type']} for animation_id: {anim['animation_id']}")

            if animations_to_play:
                # Play all animations that start at the same time concurrently
                self.play(*animations_to_play, run_time=max_duration_in_group)
                current_time += max_duration_in_group

        # Final wait to ensure the scene reaches its total duration
        if scene_total_duration > current_time:
            self.wait(scene_total_duration - current_time)
        
        # Scene transition
        self.wait(0.5)