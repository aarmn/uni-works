from manim import *

class DefaultTemplate(Scene):
    def construct(self):
        # TODO: spell out the matrix multiplication
        # TODO: show x, y plane and transform to i, 1 plane
        # TODO: real image sum part show which you pick
        # TODO: real image adding jump
        # TODO: while factoring out, indicate all of the "(cos(theta) + i sin(theta))", not just "cos(theta)" and "i sin(theta)"

        rotation_angle = "\\theta"  # Angle of rotation
        rotation_matrix = Matrix([
            [f"\\cos({rotation_angle})", f"-\\sin({rotation_angle})"],
            [f"\\sin({rotation_angle})", f"\\cos({rotation_angle})"]
        ], v_buff=1.5, h_buff=2.5, color=BLUE)  # Increased vertical and horizontal spacing

        self.play(Write(rotation_matrix))
    
        # Wait for a moment
        self.wait()
            
        # Smoothly move to final position
        self.play(
            rotation_matrix.animate.shift(LEFT*4).build ()  # Add .build()
        )

        self.wait()

        # Create matrix with a and b values
        vector_matrix = Matrix([
            ["x"],
            ["y"]
        ], v_buff=1.5, h_buff=2.5)
        
        # Create multiplication symbol
        mult_symbol = MathTex("\\times")
        mult_symbol.next_to(rotation_matrix, RIGHT)
  
        # Position it next to rotation matrix
        vector_matrix.next_to(mult_symbol, RIGHT)
        
        # Show the matrices and multiplication symbol
        self.play(
            Write(mult_symbol),
            Write(vector_matrix)
        )

        self.wait()

        # Perform matrix multiplication
        # Create equals sign
        equals = MathTex("=").next_to(vector_matrix, RIGHT)
        
        # Create result matrix showing multiplication
        result_matrix = Matrix([
            [f"x\\cos({rotation_angle}) - y\\sin({rotation_angle})"],
            [f"x\\sin({rotation_angle}) + y\\cos({rotation_angle})"]
        ], v_buff=1.5, h_buff=2.5)
        result_matrix.next_to(equals, RIGHT)
        
        # Show the result
        self.play(
            Write(equals),
            Write(result_matrix)
        )
        
        self.wait(5)

        # Fade out all objects
        self.play(
            FadeOut(rotation_matrix),
            FadeOut(mult_symbol),
            FadeOut(vector_matrix),
            FadeOut(equals),
        )

        self.play(
            result_matrix.animate.shift(UP*2 + LEFT*3).build()
        )
        # Get the elements of the result matrix and animate color change
        upper_element = result_matrix.get_entries()[0]
        lower_element = result_matrix.get_entries()[1]
        
        self.play(
            upper_element.animate.set_color(BLUE).build()
        )

        self.play(
            lower_element.animate.set_color(RED).build()
        )
        # First fade out the matrix brackets
        self.play(FadeOut(result_matrix.get_brackets()))

        # Create x and y arrows (initially transparent)
        x_arrow = MathTex("x_{new} \\rightarrow").set_opacity(0)
        y_arrow = MathTex("y_{new} \\rightarrow").set_opacity(0)
        
        # Create horizontal groups for x and y components
        x_group = VGroup(x_arrow, upper_element.copy())
        y_group = VGroup(y_arrow, lower_element.copy())
        
        # Arrange elements horizontally within groups
        x_group.arrange(RIGHT, buff=0.3)
        y_group.arrange(RIGHT, buff=0.3)
        
        # Create vertical group of the horizontal groups
        final_group = VGroup(x_group, y_group)
        final_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        final_group.move_to(ORIGIN)
        
        # Center horizontally
        shift_amount = (final_group.get_right()[0] + final_group.get_left()[0])/2
        final_group.shift(LEFT * shift_amount)
        
        # Get target positions for the elements
        upper_target = x_group[1].get_center()
        lower_target = y_group[1].get_center()
        
        # Animate elements to smoothly shift to center positions
        self.play(
            upper_element.animate.move_to(upper_target).build(),
            lower_element.animate.move_to(lower_target).build()
        )
        
        # Fade in the arrows
        self.play(
            x_arrow.animate.set_opacity(1).build(),
            y_arrow.animate.set_opacity(1).build()  
        )
        
        self.wait(4)

        # Transform x_new text to "real"
        real_text = MathTex("\\text{real} \\rightarrow").move_to(x_arrow)
        
        # Transform y_new text and add i() wrapper
        imag_expr = MathTex("\\text{imaginary} \\rightarrow i(").set_opacity(1)
        closing_paren = MathTex(")").set_opacity(1)
        
        # Calculate target positions
        imag_group = VGroup(imag_expr, lower_element, closing_paren).arrange(RIGHT, buff=0.1)

        # Create new final group with updated imaginary part
        new_final_group = VGroup(
            VGroup(real_text, upper_element),
            imag_group
        )
        new_final_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Move elements to their new positions in the final group
        self.play(
            Transform(x_arrow, real_text),
            Transform(y_arrow, imag_expr),
            lower_element.animate.move_to(imag_group[1].get_center()).build(),
            upper_element.animate.move_to(new_final_group[0][1].get_center()).build(),
            FadeIn(closing_paren)
        )

        self.wait()

        # Create the sum text and parts with initial transparency
        sum_text = MathTex("\\text{sum} =").set_opacity(0)
        real_part_x = MathTex("x", "\\cos(\\theta)").set_opacity(0)
        imag_part_x = MathTex("+", "i", "x", "\\sin(\\theta)").set_opacity(0)
        real_part_y = MathTex("+", "i", "y", "\\cos(\\theta)").set_opacity(0)
        imag_part_y = MathTex("-", "y", "\\sin(\\theta)").set_opacity(0)

        # Group all parts together for positioning
        sum_group = VGroup(sum_text, real_part_x, imag_part_x, real_part_y, imag_part_y)
        sum_group.arrange(RIGHT, buff=0.1)
        sum_group.move_to(ORIGIN).shift(DOWN * 2)  # Center and position lower

        # Animate each part to fade in one by one
        self.play(sum_text.animate.set_opacity(1).build())
        self.wait()
        self.play(real_part_x.animate.set_opacity(1).build())
        self.wait()
        self.play(imag_part_x.animate.set_opacity(1).build())
        self.wait()
        self.play(real_part_y.animate.set_opacity(1).build())
        self.wait()
        self.play(imag_part_y.animate.set_opacity(1).build())

        # Transform the negative sign to i^2
        imag_part_y_transformed = MathTex("+", "i^2", "y", "\\sin(\\theta)")
        imag_part_y_transformed.set_color_by_tex("i^2", GREEN)
        # imag_part_y_transformed.set_color_by_tex("y \\sin(\\theta)", GREEN)
        imag_part_y_transformed.next_to(real_part_y, RIGHT, buff=0.1)

        self.wait()

        self.play(Transform(imag_part_y, imag_part_y_transformed))

        self.wait()

        # write sum under the equation
        sum_under_eq = MathTex("\\text{sum} =").next_to(sum_group, DOWN, buff=0.5).shift(LEFT * 5)
        self.play(Write(sum_under_eq))

        self.wait()

        self.play(
            Indicate(real_part_x.get_parts_by_tex("x")),
            Indicate(imag_part_x.get_parts_by_tex("x"))
        )

        self.wait()

        # write first part of sum under the equation, by factoring out x, and doing so by a transform
        x_factored_sum = MathTex("x", "(", "\\cos(\\theta)", "+", "i", "\\sin(\\theta)", ")")
        x_factored_sum.next_to(sum_under_eq, RIGHT)
        self.play(TransformMatchingTex(VGroup(real_part_x, imag_part_x).copy(), x_factored_sum))
        # recenter the sum group horizontally, and not vertically
        
        self.wait()

        self.play(
            Indicate(real_part_y.get_parts_by_tex("i")),
            Indicate(imag_part_y_transformed.get_parts_by_tex("i^2")),
            Indicate(real_part_y.get_parts_by_tex("y")),
            Indicate(imag_part_y_transformed.get_parts_by_tex("y"))
        )

        self.wait()

        y_factored_sum = MathTex("+", "i", "y", "(", "\\cos(\\theta)", "+", "i", "\\sin(\\theta)", ")")
        y_factored_sum.next_to(x_factored_sum, RIGHT)
        self.play(TransformMatchingTex(VGroup(real_part_y, imag_part_y).copy(), y_factored_sum))

        self.wait()

        self.play(
            # Fade out everything except the sum_under_eq and x_factored_sum, and y_factored_sum
            # include image ->, real -> and i^2y dangling green pieces
            FadeOut(sum_group),
            FadeOut(imag_part_y_transformed),
            FadeOut(new_final_group),
            FadeOut(closing_paren),
            FadeOut(imag_expr),
            FadeOut(imag_part_y),
            FadeOut(real_text),
            FadeOut(x_arrow),
            FadeOut(y_arrow),
            FadeOut(imag_group),
        )

        self.wait()

        self.play(
            # move the sum down group to origin
            VGroup(sum_under_eq, x_factored_sum, y_factored_sum).animate.move_to(ORIGIN)
        )

        self.wait()

        # Indicate the common term (cos(theta) + i sin(theta))
        self.play(
            Indicate(x_factored_sum.get_parts_by_tex("\\cos(\\theta)")),
            Indicate(x_factored_sum.get_parts_by_tex("\\sin(\\theta)")),
            # Indicate(y_factored_sum.get_parts_by_tex("i")),
            Indicate(x_factored_sum[4]),
            Indicate(x_factored_sum.get_parts_by_tex("+")),
            Indicate(x_factored_sum.get_parts_by_tex("(")),
            Indicate(x_factored_sum.get_parts_by_tex(")")),
        )

        self.wait()

        self.play(
            Indicate(y_factored_sum.get_parts_by_tex("\\cos(\\theta)")),
            Indicate(y_factored_sum.get_parts_by_tex("\\sin(\\theta)")),
            Indicate(y_factored_sum[6]),
            Indicate(y_factored_sum.get_parts_by_tex("+")[1]),
            Indicate(y_factored_sum.get_parts_by_tex("(")),
            Indicate(y_factored_sum.get_parts_by_tex(")")),
        )

        self.wait()

        # Factor out (cos(theta) + i sin(theta)) in one tex transform
        factored_sum = MathTex("(", "x", "+", "i", "y", ")", "(", "\\cos(\\theta)", "+", "i", "\\sin(\\theta)", ")")
        factored_sum.next_to(sum_under_eq, RIGHT, buff=0.1)
        self.play(TransformMatchingTex(VGroup(x_factored_sum, y_factored_sum), factored_sum))

        self.wait()

        # recenter 
        self.play(
            VGroup(sum_under_eq, factored_sum).animate.move_to(ORIGIN)
        )

        self.wait()

        # indicate c of cos and i behind sin, and s of sin
        self.play(
            Indicate(factored_sum[7][0]),
            Indicate(factored_sum[9]),
            Indicate(factored_sum[10][0])
        )

        self.wait()

        # Factor out (cos(theta) + i sin(theta)) in one tex transform
        factored_sum_new = MathTex("(", "x", "+", "i", "y", ")", "(", "\\text{cis}(\\theta)", ")")
        factored_sum_new.next_to(sum_under_eq, RIGHT, buff=0.1)
        self.play(TransformMatchingTex(factored_sum, factored_sum_new))

        self.wait()

        self.play(
            VGroup(sum_under_eq, factored_sum_new).animate.move_to(ORIGIN)
        )

        self.wait()

        # open a bracket under the cis(theta), and write e^(i theta), using manim 
        # Create a brace under the object
        brace = Brace(factored_sum_new[7], DOWN)  # [7] is the cis(theta) part
        # Create the text to go under the brace
        brace_text = MathTex("e^{i\\theta}")
        # Put the text under the brace
        brace_text.next_to(brace, DOWN)

        # Animate both appearing
        self.play(
            Create(brace),
            Write(brace_text)
        )

        self.wait(10)

        # clear screen
        self.play(
            FadeOut(brace),
            FadeOut(brace_text),
            FadeOut(sum_under_eq),
            FadeOut(factored_sum_new)
        )

        self.wait()

        # write thanks for watching, by AARMN
        thanks_text = Text("Thanks for watching!", font_size=90).move_to(ORIGIN)
        self.play(Write(thanks_text))

        self.wait()

        by_aarmn = Text("by AARMN (Alireza Mohammadnezhad)", font_size=20).next_to(thanks_text, DOWN)
        self.play(Write(by_aarmn))

        self.wait()

        # # Recenter the sum_under_eq and x_factored_sum group horizontally with animation
        # combined_group = VGroup(sum_under_eq, x_factored_sum)
        # combined_group.arrange(RIGHT, buff=0.1)
        # self.play(combined_group.animate.shift(LEFT*2))  # Move the group slightly to the left
        # # FUCKING DUMB SHIT KEEP CENTRING THIS

        # self.wait()

        #         # Concatenate real_part_x and imag_part_x into one tex object
        # combined_part_x = MathTex("x", "\\cos(\\theta)", "+", "ix", "\\sin(\\theta)")
        # combined_part_x.set_opacity(0)
        # # Concatenate real_part_y and imag_part_y into one tex object
        # combined_part_y = MathTex("+", "i", "y", "\\cos(\\theta)", "-", "y", "\\sin(\\theta)")
        # combined_part_y.set_opacity(0)

        # # Group the combined parts together for positioning
        # combined_sum_group = VGroup(sum_text, combined_part_x, combined_part_y)
        # combined_sum_group.arrange(RIGHT, buff=0.1)
        # combined_sum_group.move_to(ORIGIN).shift(DOWN * 2)  # Center and position lower

        # # Set the opacity of the combined parts to 1 without animation
        # combined_part_x.set_opacity(1)
        # combined_part_y.set_opacity(1)

        # Factor out yi and x from the respective parts
        # factored_imag_part = MathTex("iy (\\cos(\\theta) + i \\sin(\\theta))")
        # factored_real_part = MathTex("x (\\cos(\\theta) + i \\sin(\\theta))")
        # plus_sign = MathTex("{+}")

        # Highlight the parts containing 'x'
        # real_part_x.set_color_by_tex("x", BLUE)
        # imag_part_x.set_color_by_tex("x", BLUE)
        
        # self.wait()

        # Create a new sum text object for the other line
        # sum_text_other_line = MathTex("sum =")
        # sum_text_other_line.next_to(combined_sum_group, DOWN, buff=0.5)
        # factored_real_part.next_to(sum_text_other_line, RIGHT)
        # plus_sign.next_to(factored_real_part, RIGHT)
        # factored_imag_part.next_to(plus_sign, RIGHT)

        # self.play(
        #     FadeIn(sum_text_other_line)
        # )

        # self.wait()

        # self.play(
        #     TransformMatchingTex(
        #         combined_part_x, 
        #         factored_real_part,
        #         matched_keys = ["sin(\\theta)", "cos(\\theta)", "i", "x", "y"]
        #         )
        # )

        # self.wait()

        # self.play(
        #     TransformMatchingTex(
        #         combined_part_y, 
        #         factored_imag_part,
        #         matched_keys = ["sin(\\theta)", "cos(\\theta)", "i", "x", "y"]
        #         )
        # )

        # Animate the factoring process
        # self.play(
        #     Transform(real_part_x, factored_real_part),
        #     Transform(imag_part_x, plus_sign),
        #     Transform(real_part_y, factored_imag_part),
        #     Transform(sum_text, sum_text),  # Keep sum_text as is
        #     FadeOut(imag_part_y_transformed),
        #     FadeOut(imag_part_y)
        # )
        # self.play(FadeIn(factored_sum_group))  # Fade in the factored sum group
        # self.wait()

        # # Transform y_group to imag_group
        # imag_group.move_to(y_group)
        # imag_group.align_to(y_group, LEFT)
        # imag_group.arrange(RIGHT, buff=0.1)
        

        # new_final_group.move_to(ORIGIN)

        # self.play(
        #     Transform(y_group, imag_group),
        # )

        # self.wait()
        
        # # Center horizontally
        # shift_amount = (new_final_group.get_right()[0] + new_final_group.get_left()[0])/2
        # new_final_group.shift(LEFT * shift_amount)
        
        # # Animate all elements smoothly to their new positions
        # self.play(
        #     Transform(y_arrow, imag_expr),
        #     FadeIn(closing_paren),
        #     upper_element.animate.move_to(new_final_group[0][1].get_center()).build(),
        #     lower_element.animate.move_to(new_final_group[1][1].get_center()).build()
        # )

        # self.wait()
