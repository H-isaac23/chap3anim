from manim import *
from manim_slides import Slide
import math


class Archi(Slide):
    def play_next(self):
        indicator = Arrow(buff=0.75)
        indicator.to_edge(DOWN).to_edge(RIGHT)

        self.play(FadeIn(indicator), run_time=0.75)

        self.wait(1)
        self.next_slide()
        self.play(Uncreate(indicator), run_time=0.75)

    def construct(self):
        self.camera.background_color = "#141414"
        # self.play_next()
        title = Text("Architecture", font_size=24)
        title.to_edge(UP)

        s1 = Text("Load and Preprocess PDF", font_size=24)
        s2 = Text("Embed to Vector Database", font_size=24)
        s3 = Text("Load Model, Agents, and Tools", font_size=24)
        s4 = Text("Create Chain", font_size=24)
        s5 = Text("Perform chain calls", font_size=24)
        s6 = Text("Get output", font_size=24)

        # a6 = Arrow(s1.get_edge_center(DOWN), s2.get_edge_center(UP))

        # b1 = SurroundingRectangle(s1, color=WHITE)
        # b2 = SurroundingRectangle(s2, color=WHITE)
        # b3 = SurroundingRectangle(s3, color=WHITE)
        # b4 = SurroundingRectangle(s4, color=WHITE)
        # b5 = SurroundingRectangle(s5, color=WHITE)
        # b6 = SurroundingRectangle(s6, color=WHITE)

        # n1, n2, n3, n4, n5, n6 = VGroup(s1, b1), VGroup(s2, b2), VGroup(
        #     s3, b3), VGroup(s4, b4), VGroup(s5, b5), VGroup(s6, b6)
        # s2.next_to(s3, LEFT)
        # s1.next_to(s2, LEFT)
        # s4.next_to(s3, RIGHT)
        # s5.next_to(s4, RIGHT)
        # s6.next_to(s5, RIGHT)

        s1.to_edge(LEFT).shift(UP*2)
        s2.next_to(s1, DOWN*5)
        s3.next_to(s2, RIGHT*4)
        s4.next_to(s3, RIGHT*4)
        s5.next_to(s4, DOWN*5)
        s6.next_to(s5, DOWN*5)

        a1 = Arrow(s1.get_edge_center(DOWN), s2.get_edge_center(UP))
        a2 = Arrow(s2.get_edge_center(RIGHT), s3.get_edge_center(LEFT))
        a3 = Arrow(s3.get_edge_center(RIGHT), s4.get_edge_center(LEFT))
        a4 = Arrow(s4.get_edge_center(DOWN), s5.get_edge_center(UP))
        a5 = Arrow(s5.get_edge_center(DOWN), s6.get_edge_center(UP))

        # s4.shift(UP*0.05)
        s3.shift(DOWN*0.05)

        archi = VGroup(s1, s2, s3, s4, s5, s6)
        # self.add(a1, a2, a3, a4, a5, archi, title)
        self.play(Create(archi), Create(a1), Create(a2), Create(
            a3), Create(a4), Create(a5), Create(title))
        self.play_next()

        """
        The future king is the prince
        Daughter is the princess
        Son is the prince
        """


class Preprocess(Slide):
    def play_next(self):
        indicator = Arrow(buff=0.75)
        indicator.to_edge(DOWN).to_edge(RIGHT)

        self.play(FadeIn(indicator), run_time=0.75)

        self.wait(1)
        self.next_slide()
        self.play(Uncreate(indicator), run_time=0.75)

    def construct(self):
        self.camera.background_color = "#141414"
        pre_text = Text("Preprocess the PDF", font_size=24)
        rem_text = Text("Remove stop words", font_size=24)
        low_text = Text("Lowercase all letters", font_size=24)
        ohe_text = Text("Perform one-hot-encoding", font_size=24)
        pre_text.to_edge(UP)
        rem_text.to_edge(DOWN)
        ohe_text.to_edge(DOWN)
        low_text.to_edge(DOWN)

        one_hot_encoded = Table(
            [
                ["1", "0", "0", "0", "0", "0"],
                ["0", "1", "0", "0", "0", "0"],
                ["...", "...", "...", "...", "...", "..."],
                ["0", "0", "0", "0", "0", "1"],
            ],
            col_labels=[Text("is_future"), Text("is_king"), Text("is_prince"), Text(
                "is_daughter"), Text("is_princess"), Text("is_son")],
            row_labels=[Text("future"), Text("king"), Text("..."), Text("son")]
        )
        one_hot_encoded.scale(0.5)

        one_hot_encoded_text = Text(
            "[[1, 0, 0, 0, 0, 0]\n [0, 1, 0, 0, 0, 0]\n [..., ..., ..., ..., ..., ...]\n [0, 0, 0, 0, 0, 1]]",
            font_size=24
        )

        l1 = Text("The future king is the prince", font_size=24)
        l2 = Text("Daughter is the princess", font_size=24)
        l3 = Text("Son is the prince", font_size=24)

        rl1 = Text("future king prince", font_size=24)
        rl2 = Text("Daughter princess", font_size=24)
        rl3 = Text("Son prince", font_size=24)

        ll2 = Text("daughter princess", font_size=24)
        ll3 = Text("son prince", font_size=24)

        to_table = VGroup(ll2, ll3, rl1)

        l1.next_to(l2, UP)
        l3.next_to(l2, DOWN)

        rl1.next_to(l2, UP)
        rl3.next_to(l2, DOWN)

        ll3.next_to(l2, DOWN)

        # \\\\\\\\\\\\\\\\\ NN
        c1, c2, c3, c4, c5, c6 = Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(
            radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(
            radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25)
        c3.shift(UP*0.5)
        c4.next_to(c3, 2*DOWN)
        c5.next_to(c4, 2*DOWN)
        c6.next_to(c5, 2*DOWN)
        c2.next_to(c3, 2*UP)
        c1.next_to(c2, 2*UP)

        c7, c8 = Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(
            radius=0.25, color=WHITE, stroke_width=1.25)
        c7.shift(0.5*UP)
        c8.shift(0.5*DOWN)

        c9, c10, c11, c12, c13, c14 = Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(
            radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25), Circle(
            radius=0.25, color=WHITE, stroke_width=1.25), Circle(radius=0.25, color=WHITE, stroke_width=1.25)
        c11.shift(UP*0.5)
        c12.next_to(c11, 2*DOWN)
        c13.next_to(c12, 2*DOWN)
        c14.next_to(c13, 2*DOWN)
        c10.next_to(c11, 2*UP)
        c9.next_to(c10, 2*UP)

        layer1 = VGroup(c1, c2, c3, c4, c5, c6)
        layer2 = VGroup(c7, c8)
        layer3 = VGroup(c9, c10, c11, c12, c13, c14)

        layer1.shift(2.5*LEFT)
        layer3.shift(2.5*RIGHT)

        lsin = VGroup()
        ls1 = VGroup()
        ls2 = VGroup()

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

        input_dot = Dot()
        # \\\\\\\\\\\\\\\\\\\\\\\\ End NN
        # \\\\\\\\\\\\\\\\\ start vector space

        vs_ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )

        future_dot = Dot()
        king_dot = Dot()
        prince_dot = Dot()
        daughter_dot = Dot()
        princess_dot = Dot()
        son_dot = Dot()
        future = Text("future", font_size=12)

        king = Text("king", font_size=12)

        prince = Text("prince", font_size=12)

        daughter = Text("daughter", font_size=12)

        princess = Text("princess", font_size=12)

        son = Text("son", font_size=12)

        # self.add(vs_ax, center_dot, future_dot, king_dot, prince_dot,
        #          daughter_dot, princess_dot, son_dot, future, king, prince, daughter, princess, son)

        # \\\\\\\\\\\\\\\\\ end vector space

        # //// Animation Part 1

        # self.add(l1, l2, l3, pre_text, rem_text)
        # Animation Part 1
        self.play(Create(pre_text))
        self.play_next()

        self.play(Create(l1), Create(l2), Create(l3))
        self.play_next()

        self.play(Create(rem_text), run_time=0.5)
        self.play(
            l1.animate.become(rl1),
            l2.animate.become(rl2),
            l3.animate.become(rl3)
        )
        self.play_next()

        self.play(Uncreate(rem_text), run_time=0.5)
        self.play(Create(low_text), run_time=0.5)
        self.play(l2.animate.become(ll2), l3.animate.become(ll3))
        self.remove(l1, l2, l3)
        self.add(to_table)
        self.play_next()

        self.play(Uncreate(low_text))
        self.play(Create(ohe_text))
        self.play(to_table.animate.become(one_hot_encoded))
        self.play_next()

        self.play(Uncreate(to_table), Create(one_hot_encoded_text))
        self.play_next()

        # one_hot_encoded_text.next_to(layer1, LEFT*3)
        # self.add(one_hot_encoded_text, layer1, layer2, layer3, ls1, ls2)

        # //// Animation Part 2

        self.play(one_hot_encoded_text.animate.next_to(
            layer1, LEFT*3), Uncreate(ohe_text))
        input_dot.move_to(one_hot_encoded_text.get_center())

        for n in layer1:
            start = input_dot.get_center()
            end = n.get_edge_center(LEFT)
            l = Line(start, end, stroke_width=0.75, color=GRAY)
            lsin.add(l)

        self.play(Create(layer1), Create(layer2),
                  Create(layer3), Create(ls1), Create(ls2))
        self.play_next()

        self.play(one_hot_encoded_text.animate.become(input_dot))
        self.play(ShowPassingFlash(lsin.copy().set_color(
            BLUE), run_time=0.5, time_width=0.5), Uncreate(one_hot_encoded_text), run_time=0.5)
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
        self.play_next()

        self.play(Uncreate(layer3), Uncreate(layer2), Uncreate(
            layer1), Uncreate(ls2), Uncreate(ls1))

        # //// Animation Part 3
        self.play(Create(vs_ax), run_time=1)
        self.play(LaggedStart(
            future_dot.animate.move_to(vs_ax.c2p(-0.9, -1.1)),
            king_dot.animate.move_to(vs_ax.c2p(-1.1, 0.8)),
            prince_dot.animate.move_to(vs_ax.c2p(-0.65, -1.4)),
            daughter_dot.animate.move_to(vs_ax.c2p(1.05, 0.6)),
            princess_dot.animate.move_to(vs_ax.c2p(1.1, 1)),
            son_dot.animate.move_to(vs_ax.c2p(-1.6, -0.9)),
            lag_ratio=0.25,
            run_time=1
        ))
        future.next_to(future_dot, RIGHT)
        king.next_to(king_dot, RIGHT)
        prince.next_to(prince_dot, RIGHT)
        daughter.next_to(daughter_dot, RIGHT)
        princess.next_to(princess_dot, RIGHT)
        son.next_to(son_dot, RIGHT)

        self.play(FadeIn(future), FadeIn(king), FadeIn(prince),
                  FadeIn(daughter), FadeIn(princess), FadeIn(son), run_time=0.5)
        self.play_next()

        self.play(Uncreate(future), Uncreate(king), Uncreate(prince),
                  Uncreate(daughter), Uncreate(princess), Uncreate(son), run_time=0.5)
        self.play(Uncreate(vs_ax), Uncreate(future_dot), Uncreate(king_dot), Uncreate(prince_dot),
                  Uncreate(daughter_dot), Uncreate(princess_dot), Uncreate(son_dot), run_time=0.5)
        self.play_next()


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

        lsin = VGroup()
        ls1 = VGroup()
        ls2 = VGroup()
        ls3 = VGroup()

        ls4 = VGroup()
        ls5 = VGroup()
        ls6 = VGroup()

        for n in layer1:
            line_start = n.get_edge_center(RIGHT)
            line_ends = []
            for n_j in layer2:
                line_ends.append(n_j.get_edge_center(LEFT))

            for end in line_ends:
                l = Line(line_start, end, stroke_width=0.75, color=GRAY)
                l2 = Line(end, line_start, stroke_width=0.75, color=GRAY)
                ls1.add(l)
                ls4.add(l2)

        for n in layer2:
            line_start = n.get_edge_center(RIGHT)
            line_ends = []
            for n_j in layer3:
                line_ends.append(n_j.get_edge_center(LEFT))

            for end in line_ends:
                l = Line(line_start, end, stroke_width=0.75, color=GRAY)
                l2 = Line(end, line_start, stroke_width=0.75, color=GRAY)
                ls2.add(l)
                ls5.add(l2)

        for n in layer3:
            line_start = n.get_edge_center(RIGHT)
            line_end = output_layer.get_edge_center(LEFT)
            l = Line(line_start, line_end, stroke_width=0.75, color=GRAY)
            l2 = Line(line_end, line_start, stroke_width=0.75, color=GRAY)

            ls3.add(l)
            ls6.add(l2)

        input_vec = Matrix([[2], [3]])
        input_vec.next_to(layer1, 3*LEFT).scale(0.6)
        input_dot = Dot()
        input_dot.move_to(input_vec.get_center())

        for n in layer1:
            start = input_dot.get_center()
            end = n.get_edge_center(LEFT)
            l = Line(start, end, stroke_width=0.75, color=GRAY)
            lsin.add(l)

        w1 = ValueTracker(0)
        w2 = ValueTracker(0)

        w_text = MathTex(r"w_1^{(1)}=[", font_size=22)
        w_end_text = MathTex("]", font_size=22)
        w1_text = DecimalNumber(w1.get_value(), font_size=22)
        w2_text = DecimalNumber(w2.get_value(), font_size=22)

        w1_text.next_to(w_text, RIGHT)
        w2_text.next_to(w1_text, RIGHT)
        w_end_text.next_to(w2_text, RIGHT)
        w_end_text.add_updater(
            lambda m: m.next_to(w2_text, RIGHT)
        )
        w1_text.add_updater(
            lambda m: m.set_value(w1.get_value())
        )
        w2_text.add_updater(
            lambda m: m.set_value(w2.get_value())
        )

        weights = VGroup(w_text, w_end_text, w1_text, w2_text)
        weights.to_edge(LEFT)

        # self.add(layer1, layer2, layer3, output_layer, ls1, ls2, ls3)
        # self.add(input_vec)

        # Animation Part 1
        self.play(Create(layer1), Create(layer2),
                  Create(layer3), Create(output_layer))
        self.play(Create(ls1), Create(ls2), Create(ls3))
        self.play(Create(input_vec))

        # Forward prop
        # self.play(input_vec.animate.next_to(layer1, UP))
        # self.play(input_vec.animate.shift(DOWN*2.5).set_opacity(0))
        self.play(input_vec.animate.become(input_dot), Create(weights))
        self.play(ShowPassingFlash(lsin.copy().set_color(
            BLUE), run_time=0.5, time_width=0.5), Uncreate(input_vec), run_time=0.5)
        # self.play(Create(w_text), Create(w1_text), Create(
        #     w2_text), Create(w_end_text), run_time=1)
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
        self.remove(ls1, ls2, ls3)
        self.add(ls4, ls5, ls6)
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))

        self.play(
            w1.animate.set_value(5.5), w2.animate.set_value(4.15),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 2
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(7.35), w2.animate.set_value(6.35),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 3
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(8.47), w2.animate.set_value(7.64),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 4
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(9.35), w2.animate.set_value(8.41),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 5
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(9.87), w2.animate.set_value(8.73),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 5
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(10.29), w2.animate.set_value(9.13),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 6
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(10.44), w2.animate.set_value(9.35),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 7
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(10.57), w2.animate.set_value(9.37),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 8
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(10.64),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 9
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(10.67),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        # epoch 10
        self.play(ShowPassingFlash(ls6.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls5.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(ShowPassingFlash(ls4.copy().set_color(
            YELLOW), run_time=0.25, time_width=0.5, reverse=True))
        self.play(
            w1.animate.set_value(10.68),
            run_time=0.5,
            rate_func=rate_functions.ease_in_out_cubic
        )

        self.wait(3)
