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

        """
        The future king is the prince
        Daughter is the princess
        Son is the prince
        """

        pre_text = Text("Preprocess the PDF")
        l1 = Text("The future king is the prince")
        l2 = Text("Daughter is the princess")
        l3 = Text("Son is the prince")

        # self.wait(3)
