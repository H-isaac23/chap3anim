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
        title = Text("Architecture", font_size=24)
        title.to_edge(UP)

        s1 = Text("Load and Preprocess PDF", font_size=24)
        s2 = Text("Embed to Vector Database", font_size=24)
        s3 = Text("Load Model, Agents, and Tools", font_size=24)
        s4 = Text("Create Chain", font_size=24)
        s5 = Text("Perform chain calls", font_size=24)
        s6 = Text("Get output", font_size=24)

        b1 = SurroundingRectangle(s1, color=WHITE)
        b2 = SurroundingRectangle(s2, color=WHITE)
        b3 = SurroundingRectangle(s3, color=WHITE)
        b4 = SurroundingRectangle(s4, color=WHITE)
        b5 = SurroundingRectangle(s5, color=WHITE)
        b6 = SurroundingRectangle(s6, color=WHITE)

        n1, n2, n3, n4, n5, n6 = VGroup(s1, b1), VGroup(s2, b2), VGroup(
            s3, b3), VGroup(s4, b4), VGroup(s5, b5), VGroup(s6, b6)
        n2.next_to(n3, LEFT)
        n1.next_to(n2, LEFT)

        n4.next_to(n3, RIGHT)
        n5.next_to(n4, RIGHT)
        n6.next_to(n5, RIGHT)

        archi = VGroup(n1, n2, n3, n4, n5, n6)
        self.add(archi)
