from manim import *
from manim_slides import Slide
import math


class Count(Animation):
    def __init__(self, num: DecimalNumber, to_value, **kwargs):
        super().__init__(num, **kwargs)
        self.to_value = to_value

    def interpolate_mobject(self, alpha: float) -> None:
        # val = self.mobject.get_value() + (alpha*self.to_value)
        self.mobject.set_value(self.to_value)


class PartOne(Slide):
    def play_next(self):
        indicator = Arrow(buff=0.75)
        indicator.to_edge(DOWN).to_edge(RIGHT)

        self.play(FadeIn(indicator), run_time=0.75)

        self.wait(1)
        self.next_slide()
        self.play(Uncreate(indicator), run_time=0.75)

    def construct(self):
        self.camera.background_color = "#141414"
        # self.wait()
        # self.next_slide()
        self.play_next()

        title = Text("Math Behind The Study (Neural Networks)", color=WHITE)
        self.play(Create(title))
        self.wait(1)

        self.play(title.animate.scale(0.75))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        t1 = Text("1. Activation Functions").set_color(WHITE)

        t2 = Text("2. Cost Functions").set_color(WHITE)

        t3 = Text("3. Gradient Descent & Backpropagation").set_color(WHITE)

        t4 = Text("4. Word Embeddings").set_color(WHITE)

        t5 = Text("5. Transformer Model").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4, t5).arrange(
            direction=DOWN, aligned_edge=LEFT).scale(0.7)

        self.play(Create(x.submobjects[0]))
        self.play_next()

        self.play(Create(x.submobjects[1]))
        self.play_next()

        self.play(Create(x.submobjects[2]))
        self.play_next()

        self.play(Create(x.submobjects[3]))
        self.play_next()

        self.play(Create(x.submobjects[4]))
        self.play_next()

        self.play(x.animate.set_opacity(0.25))
        self.play(x.submobjects[0].animate.set_opacity(1).scale(1.1))
        self.play_next()

        self.play(x.animate.set_opacity(1),
                  x.submobjects[0].animate.scale(1.0/1.1))
        self.play(FadeOut(x), FadeOut(title))
        self.wait(1)


class AFunc(Slide):
    def play_next(self):
        indicator = Arrow(buff=0.75)
        indicator.to_edge(DOWN).to_edge(RIGHT)

        self.play(FadeIn(indicator), run_time=0.75)

        self.wait(1)
        self.next_slide()
        self.play(Uncreate(indicator), run_time=0.75)

    def construct(self):
        self.camera.background_color = "#141414"
        self.play_next()

        # Sigmoid Function
        sig_title = Text("Sigmoid Function")
        sig_title.to_edge(UP).scale(0.8)

        sig_eq = MathTex(r"\frac{1}{1+e^{-z}}")
        z_def = MathTex('z = wx + b')
        z_meaning = Text(
            "'w' and 'b' are the weights and biases.", font_size=24)
        z_meaning.next_to(z_def, DOWN)

        sig_use = Text("Mainly used in binary classification.", font_size=24)

        # Animation Part 1
        self.play(Create(sig_title))
        self.wait(1)

        self.play(Create(sig_eq))
        self.wait(1)

        self.play(sig_eq.animate.to_edge(LEFT))
        self.play(FadeIn(z_def), FadeIn(z_meaning))
        self.play_next()

        self.play(FadeOut(z_def, z_meaning))
        self.play(FadeIn(sig_use))
        self.play_next()

        self.play(Uncreate(sig_use), Uncreate(sig_eq),
                  sig_title.animate.to_edge(LEFT))
        self.wait(1)

        # Part 2

        t = ValueTracker(0)
        dot = Dot()

        ax = Axes(
            x_range=[-10, 10],
            y_range=[0, 1]
        )

        def sig(x):
            return 1/(1+((math.e) ** -x))

        # graph and dot
        graph = ax.plot(lambda x: sig(x),
                        x_range=[-10, 10], color=BLUE)

        dot.move_to(ax.c2p(t.get_value(), sig(t.get_value())))
        dot.add_updater(
            lambda m: m.move_to(ax.c2p(t.get_value(), sig(t.get_value())))
        )

        # where dot moves
        # funcrange = np.linspace(0, 7, 200)
        # max_index = sig(funcrange).argmax()

        # Text to render
        sig_prob = DecimalNumber(
            sig(t.get_value()), num_decimal_places=3)
        sig_prob.add_updater(
            lambda m: m.set_value(sig(t.get_value()))
        )
        sig_x_val = DecimalNumber(
            t.get_value(), num_decimal_places=3)
        sig_x_val.add_updater(
            lambda m: m.set_value((t.get_value()*2.5)+80)
        )

        sig_prob_text_1 = MathTex('P( ')
        sig_prob_text_2 = MathTex(') = ')
        sig_prob.to_edge(RIGHT)
        sig_prob_text_2.next_to(sig_prob, LEFT)
        sig_x_val.next_to(sig_prob_text_2, LEFT)

        sig_x_val.add_updater(
            lambda m: m.next_to(sig_prob_text_2, LEFT)
        )

        sig_prob_text_1.add_updater(
            lambda m: m.next_to(sig_x_val, LEFT)
        )

        sig_prob_text_1.next_to(sig_x_val, LEFT)

        # Animation Part 2
        self.play(Create(ax), Create(graph), run_time=2)
        self.play(Create(dot))
        self.play_next()

        self.play(Flash(dot))
        self.play_next()

        self.play(Create(sig_prob_text_1), Create(sig_prob_text_2),
                  Create(sig_x_val), Create(sig_prob))
        self.play(
            t.animate.set_value(5.5),
            run_time=3,
            rate_func=rate_functions.ease_in_out_cubic)
        self.play_next()

        self.play(
            t.animate.set_value(-3),
            run_time=3,
            rate_func=rate_functions.ease_in_out_cubic
        )

        self.play_next()

        self.play(FadeOut(ax, graph, dot, sig_prob_text_1,
                  sig_prob_text_2, sig_eq, sig_x_val, sig_title, sig_prob))
        self.wait(2)

        # self.play()


class NN(Slide):
    def play_next(self):
        indicator = Arrow(buff=0.75)
        indicator.to_edge(DOWN).to_edge(RIGHT)

        self.play(FadeIn(indicator), run_time=0.75)

        self.wait(1)
        self.next_slide()
        self.play(Uncreate(indicator), run_time=0.75)

    def construct(self):
        self.camera.background_color = "#141414"

        c1, c2, c3 = Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(
            radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25)
        c1.next_to(c2, 2*UP)
        c3.next_to(c2, 2*DOWN)

        layer1 = VGroup(c1, c2, c3)
        layer2 = layer1.copy()
        layer3 = layer2.copy()
        output_layer = Circle(radius=0.25, stroke_width=1.25, color=WHITE)

        layer1.shift(2.5*LEFT)
        layer3.shift(2.5*RIGHT)
        output_layer.shift(5*RIGHT)

        ls1 = VGroup()
        ls2 = VGroup()
        ls3 = VGroup()

        for n in layer1:
            line_start = n.get_edge_center(RIGHT)
            line_ends = []
            for n_j in layer2:
                line_ends.append(n_j.get_edge_center(LEFT))

            for end in line_ends:
                l = Line(line_start, end, stroke_width=0.75, color=GRAY)
                ls1.add(l)

        for n in layer2:
            line_start = n.get_edge_center(RIGHT)
            line_ends = []
            for n_j in layer3:
                line_ends.append(n_j.get_edge_center(LEFT))

            for end in line_ends:
                l = Line(line_start, end, stroke_width=0.75, color=GRAY)
                ls2.add(l)

        for n in layer3:
            line_start = n.get_edge_center(RIGHT)
            line_end = output_layer.get_edge_center(LEFT)
            l = Line(line_start, line_end, stroke_width=0.75, color=GRAY)
            ls3.add(l)

        input_vec = Matrix([[2], [3]])
        input_vec.next_to(layer1, 3*LEFT).scale(0.6)

        # self.add(layer1, layer2, layer3, output_layer, ls1, ls2, ls3)
        # self.add(input_vec)
        self.play(Create(layer1), Create(layer2),
                  Create(layer3), Create(output_layer))
        self.play(Create(ls1), Create(ls2), Create(ls3))
        self.play(Create(input_vec))

        # Forward prop
        self.play(input_vec.animate.next_to(layer1, UP))
        self.play(input_vec.animate.shift(DOWN*2.5).set_opacity(0))
        self.play(layer1.animate.set_fill(
            WHITE, opacity=0.5), run_time=0.25)
        self.play(layer1.animate.set_fill(
            WHITE, opacity=0), run_time=0.25)
        self.play(ShowPassingFlash(ls1.copy().set_color(
            BLUE), run_time=0.5, time_width=0.5))
        self.play(layer2.animate.set_fill(
            WHITE, opacity=0.5), run_time=0.25)
        self.play(layer2.animate.set_fill(
            WHITE, opacity=0), run_time=0.25)
        self.play(ShowPassingFlash(ls2.copy().set_color(
            BLUE), run_time=0.5, time_width=0.5))
        self.play(layer3.animate.set_fill(
            WHITE, opacity=0.5), run_time=0.25)
        self.play(layer3.animate.set_fill(
            WHITE, opacity=0), run_time=0.25)
        self.play(ShowPassingFlash(ls3.copy().set_color(
            BLUE), run_time=0.5, time_width=0.5))
        self.play(output_layer.animate.set_fill(
            WHITE, opacity=0.5), run_time=0.25)
        self.play(output_layer.animate.set_fill(
            WHITE, opacity=0), run_time=0.25)

        # Backprop

        self.wait(3)


# class Example(Slide):
#     def construct(self):
#         text = Text("Hello World!")
#         self.wait()

#         self.next_slide()
#         self.play(Create(text))

#         self.next_slide()
#         self.play(Uncreate(text))

# class BasicExample(Slide):
#     def construct(self):
#         circle = Circle(radius=3, color=BLUE)
#         dot = Dot()

#         self.play(GrowFromCenter(circle))
#         self.next_slide()  # Waits user to press continue to go to the next slide

#         self.start_loop()  # Start loop
#         self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
#         self.end_loop()  # This will loop until user inputs a key

#         self.play(dot.animate.move_to(ORIGIN))
#         self.next_slide()  # Waits user to press continue to go to the next slide


# class MultipleAnimationsInLastSlide(Slide):
#     """This is used to check against solution for issue #161."""

#     def construct(self):
#         circle = Circle(color=BLUE)
#         dot = Dot()

#         self.play(GrowFromCenter(circle))
#         self.play(FadeIn(dot))
#         self.next_slide()

#         self.play(dot.animate.move_to(RIGHT))
#         self.play(dot.animate.move_to(UP))
#         self.play(dot.animate.move_to(LEFT))
#         self.play(dot.animate.move_to(DOWN))

#         self.next_slide()
