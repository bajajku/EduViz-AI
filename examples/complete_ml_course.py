from manim import *

class CombinedVideo(Scene):
    """
    Machine Learning Complete Course
    Multi-scene video with 5 parts
    
    Total Duration: 72.0 seconds
    Number of Scenes: 5
    """
    
    def construct(self):
        """Main video construction with multiple scenes."""
        # Title card
        title = Text("Machine Learning Complete Course", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Play all scenes in sequence
        self.scene_1()
        self.scene_2()
        self.scene_3()
        self.scene_4()
        self.scene_5()
        
        # End card
        end_text = Text("End", font_size=36)
        self.play(FadeIn(end_text))
        self.wait(1)

    def scene_1(self):
        """Scene 1: Introduction to Machine Learning"""
        # Clear previous scene
        self.clear()
        
        # Scene content
        self.camera.background_color = BLACK

        # Object Creation
        title_ml = Text("Machine Learning", font_size=40)
        title_ml.set_max_width(11)
        title_ml.move_to([0.00, 2.50, 0])
        title_ml.set_color(WHITE)
        title_ml.set_opacity(1.0)

        def_line1 = Text("Automates Analytical Model Building", font_size=32)
        def_line1.set_max_width(11)
        def_line1.move_to([0.00, 1.00, 0])
        def_line1.set_color(WHITE)
        def_line1.set_opacity(1.0)

        def_line2 = Text("Learns from Data & Identifies Patterns", font_size=32)
        def_line2.set_max_width(11)
        def_line2.move_to([0.00, 0.00, 0])
        def_line2.set_color(WHITE)
        def_line2.set_opacity(1.0)

        def_line3 = Text("Makes Decisions with Minimal Human Intervention", font_size=32)
        def_line3.set_max_width(10)
        def_line3.move_to([0.00, -1.00, 0])
        def_line3.set_color(WHITE)
        def_line3.set_opacity(1.0)

        # Animation Timeline
        current_time = 0.0

        # Animation for title_ml (FadeIn)
        start_time = 0.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(FadeIn(title_ml), run_time=1.0)
        current_time = start_time + 1.0

        # Animation for def_line1 (Write)
        start_time = 1.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(def_line1), run_time=2.0)
        current_time = start_time + 2.0

        # Animation for def_line2 (Write)
        start_time = 3.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(def_line2), run_time=2.0)
        current_time = start_time + 2.0

        # Animation for def_line3 (Write)
        start_time = 5.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(def_line3), run_time=2.5)
        current_time = start_time + 2.5

        scene_duration = 10.0
        if scene_duration > current_time:
            self.wait(scene_duration - current_time)
        
        # Scene transition
        self.wait(0.5)
    def scene_2(self):
        """Scene 2: Supervised Learning: Learning from Labeled Data"""
        # Clear previous scene
        self.clear()
        
        # Scene content
        self.camera.background_color = BLACK

        # Object Creation
        # Using a dictionary to store objects for easy access
        manim_objects = {}

        scene_title = Text(
            "Supervised Learning: Learning from Labeled Data",
            font_size=40,
            color=YELLOW
        )
        scene_title.set_max_width(11)
        scene_title.move_to([0.00, 3.50, 0])
        manim_objects["scene_title"] = scene_title

        def_intro = Text(
            "Supervised learning is the machine learning task of learning a function\nthat maps an input to an output based on example input-output pairs.",
            font_size=24,
            color=WHITE,
            line_spacing=0.8
        )
        def_intro.set_max_width(10)
        def_intro.move_to([0.00, 2.00, 0])
        manim_objects["def_intro"] = def_intro

        def_infer = Text(
            "It infers a function from labeled training data consisting of a set of training examples.",
            font_size=24,
            color=WHITE,
            line_spacing=0.8
        )
        def_infer.set_max_width(10)
        def_infer.move_to([0.00, 0.70, 0])
        manim_objects["def_infer"] = def_infer

        algorithms_header = Text(
            "Common algorithms include:",
            font_size=24,
            color=WHITE
        )
        algorithms_header.set_max_width(11)
        algorithms_header.move_to([-3.50, -0.50, 0])
        manim_objects["algorithms_header"] = algorithms_header

        algo_lr = Text(
            "- Linear Regression",
            font_size=20,
            color=BLUE
        )
        algo_lr.set_max_width(12)
        algo_lr.move_to([-2.00, -1.30, 0])
        manim_objects["algo_lr"] = algo_lr

        algo_logr = Text(
            "- Logistic Regression",
            font_size=20,
            color=BLUE
        )
        algo_logr.set_max_width(12)
        algo_logr.move_to([-2.00, -2.10, 0])
        manim_objects["algo_logr"] = algo_logr

        algo_dt = Text(
            "- Decision Trees",
            font_size=20,
            color=BLUE
        )
        algo_dt.set_max_width(12)
        algo_dt.move_to([-2.00, -2.90, 0])
        manim_objects["algo_dt"] = algo_dt

        algo_rf = Text(
            "- Random Forests",
            font_size=20,
            color=BLUE
        )
        algo_rf.set_max_width(12)
        algo_rf.move_to([-2.00, -2.90, 0])
        manim_objects["algo_rf"] = algo_rf

        algo_svm = Text(
            "- Support Vector Machines",
            font_size=20,
            color=BLUE
        )
        algo_svm.set_max_width(11)
        algo_svm.move_to([-2.00, -3.50, 0])
        manim_objects["algo_svm"] = algo_svm

        goal_text = Text(
            "The goal is to approximate the mapping function so well that when you have\nnew input data, you can predict the output variables for that data.",
            font_size=24,
            color=GREEN,
            line_spacing=0.8
        )
        goal_text.set_max_width(10)
        goal_text.move_to([0.00, -2.10, 0])
        manim_objects["goal_text"] = goal_text

        # Animation Timeline
        current_time = 0.0

        # Animation for scene_title
        start_time = 0.0
        duration = 1.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Create(manim_objects["scene_title"]), run_time=duration)
        current_time = start_time + duration

        # Animation for def_intro
        start_time = 0.5
        duration = 3.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["def_intro"]), run_time=duration)
        current_time = max(current_time, start_time) + duration

        # Animation for def_infer
        start_time = 3.5
        duration = 3.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["def_infer"]), run_time=duration)
        current_time = start_time + duration

        # Animation for algorithms_header
        start_time = 7.0
        duration = 1.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["algorithms_header"]), run_time=duration)
        current_time = start_time + duration

        # Animation for algo_lr
        start_time = 9.0
        duration = 0.8
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["algo_lr"]), run_time=duration)
        current_time = start_time + duration

        # Animation for algo_logr
        start_time = 9.8
        duration = 0.8
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["algo_logr"]), run_time=duration)
        current_time = start_time + duration

        # Animation for algo_dt
        start_time = 10.6
        duration = 0.8
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["algo_dt"]), run_time=duration)
        current_time = start_time + duration

        # Animation for algo_rf
        start_time = 11.4
        duration = 0.8
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["algo_rf"]), run_time=duration)
        current_time = start_time + duration

        # Animation for algo_svm
        start_time = 12.2
        duration = 0.8
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["algo_svm"]), run_time=duration)
        current_time = start_time + duration

        # Fade out algorithm list to make space for the goal text
        start_time_goal = 13.5
        if start_time_goal > current_time:
            fade_out_duration = start_time_goal - current_time
            algo_group = VGroup(
                manim_objects["algorithms_header"],
                manim_objects["algo_lr"],
                manim_objects["algo_logr"],
                manim_objects["algo_dt"],
                manim_objects["algo_rf"],
                manim_objects["algo_svm"]
            )
            self.play(FadeOut(algo_group), run_time=fade_out_duration)
            current_time += fade_out_duration

        # Animation for goal_text
        start_time = 13.5
        duration = 3.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(manim_objects["goal_text"]), run_time=duration)
        current_time = start_time + duration

        # Final wait to match total duration
        total_duration = 18.0
        if total_duration > current_time:
            self.wait(total_duration - current_time)
        
        # Scene transition
        self.wait(0.5)
    def scene_3(self):
        """Scene 3: Unsupervised Learning: Discovering Hidden Patterns"""
        # Clear previous scene
        self.clear()
        
        # Scene content
        self.camera.background_color = BLACK
        current_time = 0.0
        scene_total_duration = 17.0

        # Object Creation
        scene_title = Text("Unsupervised Learning: Discovering Hidden Patterns", font_size=40)
        scene_title.set_max_width(12)
        scene_title.move_to([0.00, 3.20, 0])
        scene_title.set_color(YELLOW)

        definition_text = Text(
            "Unsupervised learning is a type of machine learning that looks for previously undetected patterns in a data set with no pre-existing labels and with a minimum of human supervision.",
            font_size=24,
            line_spacing=0.8
        )
        definition_text.set_max_width(12)
        definition_text.move_to([0.00, 1.50, 0])
        definition_text.set_color(WHITE)

        techniques_header = Text("Common techniques include:", font_size=32)
        techniques_header.set_max_width(6)
        techniques_header.move_to([-4.00, 0.00, 0])
        techniques_header.set_color(BLUE)

        clustering_text = Text("• Clustering", font_size=24)
        clustering_text.set_max_width(5)
        clustering_text.move_to([-3.50, -0.80, 0])
        clustering_text.set_color(GREEN)

        association_text = Text("• Association Rule Learning", font_size=24)
        association_text.set_max_width(5)
        association_text.move_to([-3.50, -1.60, 0])
        association_text.set_color(GREEN)

        dimensionality_text = Text("• Dimensionality Reduction", font_size=24)
        dimensionality_text.set_max_width(5)
        dimensionality_text.move_to([-3.50, -2.40, 0])
        dimensionality_text.set_color(GREEN)

        kmeans_header = Text("K-means Clustering:", font_size=28)
        kmeans_header.set_max_width(5)
        kmeans_header.move_to([3.00, -1.60, 0])
        kmeans_header.set_color(PURPLE)

        kmeans_explanation = Text("groups data points into clusters based on similarity.", font_size=24)
        kmeans_explanation.set_max_width(5)
        kmeans_explanation.move_to([3.00, -2.40, 0])
        kmeans_explanation.set_color(WHITE)

        pca_header = Text("Principal Component Analysis (PCA):", font_size=28)
        pca_header.set_max_width(5)
        pca_header.move_to([3.00, -2.40, 0])
        pca_header.set_color(PURPLE)

        pca_explanation = Text("reduces the dimensionality of data while preserving important information.", font_size=24)
        pca_explanation.set_max_width(5)
        pca_explanation.move_to([3.00, -3.20, 0])
        pca_explanation.set_color(WHITE)

        # Animation Timeline

        # Animation for scene_title (start: 0.0s, duration: 1.5s)
        start_time = 0.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(scene_title), run_time=1.5)
        current_time = start_time + 1.5

        # Animation for definition_text (start: 1.5s, duration: 4.0s)
        start_time = 1.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(definition_text), run_time=4.0)
        current_time = start_time + 4.0

        # Animation for techniques_header (start: 6.0s, duration: 1.0s)
        start_time = 6.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(techniques_header), run_time=1.0)
        current_time = start_time + 1.0

        # Animation for clustering_text (start: 7.0s, duration: 1.0s)
        start_time = 7.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(clustering_text), run_time=1.0)
        current_time = start_time + 1.0

        # Animation for kmeans_header (start: 7.5s, duration: 1.0s)
        start_time = 7.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(kmeans_header), run_time=1.0)
        current_time = start_time + 1.0

        # Animation for association_text (start: 8.0s, duration: 1.5s)
        start_time = 8.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(association_text), run_time=1.5)
        current_time = start_time + 1.5

        # Animation for kmeans_explanation (start: 8.5s, duration: 2.0s)
        start_time = 8.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(kmeans_explanation), run_time=2.0)
        current_time = start_time + 2.0

        # Animation for dimensionality_text (start: 9.5s, duration: 2.0s)
        start_time = 9.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(dimensionality_text), run_time=2.0)
        current_time = start_time + 2.0

        # Animation for pca_header (start: 10.5s, duration: 1.0s)
        start_time = 10.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(pca_header), run_time=1.0)
        current_time = start_time + 1.0

        # Animation for pca_explanation (start: 11.5s, duration: 2.5s)
        start_time = 11.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(pca_explanation), run_time=2.5)
        current_time = start_time + 2.5

        if scene_total_duration > current_time:
            self.wait(scene_total_duration - current_time)
        
        # Scene transition
        self.wait(0.5)
    def scene_4(self):
        """Scene 4: Neural Networks: Mimicking the Brain"""
        # Clear previous scene
        self.clear()
        
        # Scene content
        self.camera.background_color = BLACK

        # Object Creation
        objects = {}

        # Text objects
        scene_title = Text("Neural Networks: Mimicking the Brain", font_size=40)
        scene_title.set_max_width(11)
        scene_title.move_to([0.00, 3.50, 0])
        scene_title.set_color(WHITE)
        scene_title.set_opacity(1.0)
        objects['scene_title'] = scene_title

        input_label = Text("Input Layer", font_size=24)
        input_label.set_max_width(12)
        input_label.move_to([-4.00, 2.00, 0])
        input_label.set_color(BLUE_E)
        input_label.set_opacity(1.0)
        objects['input_label'] = input_label

        hidden_label = Text("Hidden Layers", font_size=24)
        hidden_label.set_max_width(12)
        hidden_label.move_to([0.00, 2.80, 0])
        hidden_label.set_color(GREEN_E)
        hidden_label.set_opacity(1.0)
        objects['hidden_label'] = hidden_label

        output_label = Text("Output Layer", font_size=24)
        output_label.set_max_width(12)
        output_label.move_to([4.00, 1.20, 0])
        output_label.set_color(RED_E)
        output_label.set_opacity(1.0)
        objects['output_label'] = output_label

        activation_text = Text("Activation Function", font_size=32)
        activation_text.set_max_width(11)
        activation_text.move_to([2.50, -3.00, 0])
        activation_text.set_color(YELLOW)
        activation_text.set_opacity(1.0)
        objects['activation_text'] = activation_text

        # Circle (Node) objects
        node_radius = 0.35
        objects['input_node_0'] = Circle(radius=node_radius, color=BLUE).move_to([-4, 1.0, 0]).set_fill(BLUE, opacity=1.0)
        objects['input_node_1'] = Circle(radius=node_radius, color=BLUE).move_to([-4, 0.0, 0]).set_fill(BLUE, opacity=1.0)
        objects['input_node_2'] = Circle(radius=node_radius, color=BLUE).move_to([-4, -1.0, 0]).set_fill(BLUE, opacity=1.0)

        objects['hidden_node_0'] = Circle(radius=node_radius, color=GREEN).move_to([0, 1.5, 0]).set_fill(GREEN, opacity=1.0)
        objects['hidden_node_1'] = Circle(radius=node_radius, color=GREEN).move_to([0, 0.5, 0]).set_fill(GREEN, opacity=1.0)
        objects['hidden_node_2'] = Circle(radius=node_radius, color=GREEN).move_to([0, -0.5, 0]).set_fill(GREEN, opacity=1.0)
        objects['hidden_node_3'] = Circle(radius=node_radius, color=GREEN).move_to([0, -1.5, 0]).set_fill(GREEN, opacity=1.0)

        objects['output_node_0'] = Circle(radius=node_radius, color=RED).move_to([4, 0.5, 0]).set_fill(RED, opacity=1.0)
        objects['output_node_1'] = Circle(radius=node_radius, color=RED).move_to([4, -0.5, 0]).set_fill(RED, opacity=1.0)

        # Line objects
        line_color = GRAY
        line_opacity = 0.7
        input_nodes = [objects['input_node_0'], objects['input_node_1'], objects['input_node_2']]
        hidden_nodes = [objects['hidden_node_0'], objects['hidden_node_1'], objects['hidden_node_2'], objects['hidden_node_3']]
        output_nodes = [objects['output_node_0'], objects['output_node_1']]

        lines_i_h = VGroup()
        for i_node in input_nodes:
            for h_node in hidden_nodes:
                lines_i_h.add(Line(i_node.get_center(), h_node.get_center(), color=line_color, stroke_opacity=line_opacity))

        lines_h_o = VGroup()
        for h_node in hidden_nodes:
            for o_node in output_nodes:
                lines_h_o.add(Line(h_node.get_center(), o_node.get_center(), color=line_color, stroke_opacity=line_opacity))

        all_lines = VGroup(lines_i_h, lines_h_o)

        # Animation Timeline
        current_time = 0.0

        # Time: 0.0s
        if 0.0 > current_time:
                self.wait(0.0 - current_time)
        self.play(Create(scene_title), run_time=1.5)
        current_time = 1.5

        # Time: 0.5s (played sequentially after previous animation)
        input_nodes_vg = VGroup(objects['input_node_0'], objects['input_node_1'], objects['input_node_2'])
        hidden_nodes_vg = VGroup(objects['hidden_node_0'], objects['hidden_node_1'], objects['hidden_node_2'], objects['hidden_node_3'])
        output_nodes_vg = VGroup(objects['output_node_0'], objects['output_node_1'])

        self.play(
            Create(input_nodes_vg),
            Create(hidden_nodes_vg),
            Create(output_nodes_vg),
            Flash(objects['hidden_node_2']),
            run_time=1.0
        )
        current_time += 1.0

        # Time: 1.0s (played sequentially after previous animation)
        labels_vg = VGroup(objects['input_label'], objects['hidden_label'], objects['output_label'])

        self.play(
            FadeIn(labels_vg),
            Create(all_lines),
            Write(activation_text),
            run_time=2.0
        )
        current_time += 2.0

        # Final wait to reach total duration
        if 15.0 > current_time:
                self.wait(15.0 - current_time)
        
        # Scene transition
        self.wait(0.5)
    def scene_5(self):
        """Scene 5: Deep Learning: Advanced Neural Networks"""
        # Clear previous scene
        self.clear()
        
        # Scene content
        self.camera.background_color = BLACK

        # Object Creation
        scene_title = Text("Deep Learning: Advanced Neural Networks", font_size=40)
        scene_title.set_max_width(11)
        scene_title.move_to([0.00, 2.50, 0])
        scene_title.set_color(YELLOW)

        intro_dl_text = Text("Deep learning is a subset of machine learning methods based on artificial neural networks.", font_size=24)
        intro_dl_text.set_max_width(10)
        intro_dl_text.move_to([0.00, 1.00, 0])
        intro_dl_text.set_color(WHITE)

        architectures_header = Text("Key Architectures:", font_size=32)
        architectures_header.set_max_width(12)
        architectures_header.move_to([-4.00, -0.50, 0])
        architectures_header.set_color(BLUE)

        dnn_text = Text("• Deep Neural Networks (DNNs)", font_size=24)
        dnn_text.set_max_width(11)
        dnn_text.move_to([-3.50, -1.30, 0])
        dnn_text.set_color(WHITE)

        dbn_text = Text("• Deep Belief Networks (DBNs)", font_size=24)
        dbn_text.set_max_width(11)
        dbn_text.move_to([-3.50, -2.10, 0])
        dbn_text.set_color(WHITE)

        rnn_text = Text("• Recurrent Neural Networks (RNNs)", font_size=24)
        rnn_text.set_max_width(11)
        rnn_text.move_to([-3.50, -2.90, 0])
        rnn_text.set_color(WHITE)

        cnn_text = Text("• Convolutional Neural Networks (CNNs)", font_size=24)
        cnn_text.set_max_width(11)
        cnn_text.move_to([-3.50, -3.50, 0])
        cnn_text.set_color(WHITE)

        cnn_highlight_text = Text("CNNs are particularly effective for image recognition.", font_size=24)
        cnn_highlight_text.set_max_width(10)
        cnn_highlight_text.move_to([0.00, -2.90, 0])
        cnn_highlight_text.set_color(GREEN)

        # Animation Timeline
        current_time = 0.0

        # Animation: create_title
        start_time = 0.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Create(scene_title), run_time=1.0)
        current_time = start_time + 1.0

        # Animation: write_intro
        start_time = 1.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(intro_dl_text), run_time=2.0)
        current_time = start_time + 2.0

        # Animation: fade_in_arch_header
        start_time = 4.0
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(FadeIn(architectures_header), run_time=0.5)
        current_time = start_time + 0.5

        # Animation: write_dnn
        start_time = 4.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(dnn_text), run_time=1.0)
        current_time = start_time + 1.0

        # Animation: write_dbn
        start_time = 5.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(dbn_text), run_time=1.0)
        current_time = start_time + 1.0

        # Animation: write_rnn
        start_time = 6.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(rnn_text), run_time=1.0)
        current_time = start_time + 1.0

        # Animation: write_cnn
        start_time = 7.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Write(cnn_text), run_time=1.0)
        current_time = start_time + 1.0

        # Animation: flash_cnn
        start_time = 8.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Flash(cnn_text), run_time=1.0)
        current_time = start_time + 1.0

        # Animation: create_cnn_focus
        start_time = 9.5
        if start_time > current_time:
            self.wait(start_time - current_time)
        self.play(Create(cnn_highlight_text), run_time=1.5)
        current_time = start_time + 1.5

        # Final wait to match total duration
        total_duration = 12.0
        if total_duration > current_time:
            self.wait(total_duration - current_time)
        
        # Scene transition
        self.wait(0.5)