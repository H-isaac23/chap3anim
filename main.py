from manim import *
from manim_slides import Slide

class PartOne(Slide):
    def construct(self):
        self.camera.background_color = "#141414"
        self.wait()
        self.next_slide()

        title = Text("Current Topic", color=WHITE)
        self.play(Create(title))
        self.wait(1)
        self.next_slide()

        self.play(title.animate.scale(0.75))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        self.next_slide()

        t1 = Text("1. Activation Functions").set_color(WHITE)

        t2 = Text("2. Cost Functions").set_color(WHITE)

        t3 = Text("3. Gradient Descent & Backpropagation").set_color(WHITE)

        t4 = Text("4. Word Embeddings").set_color(WHITE)

        t5 = Text("5. Transformer Model").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4, t5).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7)
        for text in x.submobjects:
            self.play(Create(text))
            self.wait(1)
            self.next_slide()
        
        self.play(x.animate.set_opacity(0.25))
        self.play(x.submobjects[0].animate.set_opacity(1))
        self.wait(1)

        self.next_slide()

        self.play(x.animate.set_opacity(1))
        self.play(FadeOut(x), FadeOut(title))
        self.wait(1)

        self.next_slide()
        

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