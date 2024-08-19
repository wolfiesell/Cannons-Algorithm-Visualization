from manim import *

def createBlankTextbox():
    result = VGroup()  
    box = Rectangle(  
        height=1, width=1, fill_color=BLUE, 
        fill_opacity=0.5, stroke_color=BLUE
    )
    
    result.add(box)
    return result

def createBlankMatrix():
    matrix = VGroup()
    box_list = []
    for i in range(9):
        box_list.append(createBlankTextbox())
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=0.25)
    return matrix

def createTextbox(number, text_color):
    result = VGroup()  # create a VGroup
    box = Rectangle(  # create a box
        height=1, width=1, fill_color=BLUE, 
        fill_opacity=0.5, stroke_color=BLUE
    )
    number_text = Text(str(number), font_size=24, color=text_color)
    result.add(box, number_text)
    return result

def createTextbox333(number, text_color):
    result = VGroup()  # create a VGroup
    box = Rectangle(  # create a box
        height=1, width=1, fill_color=BLUE, 
        fill_opacity=0.5, stroke_color=BLUE
    )
    number_text = Text(str(number), font_size=24, color=text_color)
    result.add(box, number_text)
    #product_text.align_to(box[0], DL).shift(UP * 0.1 + RIGHT * 0.1)
    number_text.align_to(box, DL).shift(UP * 0.1 + RIGHT * 0.1)
    return result

def createMatrix(textColor):
    matrix = VGroup()
    box_list = []
    for x in range(9):
        box_list.append(createTextbox(x, textColor))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=0.25)
    return matrix

def createFinalMatrix(textColor):
    matrix = VGroup()
    box_list = []
    
    box_list.append(createTextbox(15, textColor))
    box_list.append(createTextbox(18, textColor))
    box_list.append(createTextbox(21, textColor))
    box_list.append(createTextbox(42, textColor))
    box_list.append(createTextbox(54, textColor))
    box_list.append(createTextbox(66, textColor))
    box_list.append(createTextbox(69, textColor))
    box_list.append(createTextbox(90, textColor))
    box_list.append(createTextbox(111, textColor))

    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=0.25)
    return matrix


def createCustomDoubledTextbox(number1, number2, text_color_right, text_color_left):
    result = VGroup()
    box = Rectangle(
        height=1, width=1, fill_color=BLUE,
        fill_opacity=0.5, stroke_color=BLUE
    )
    number_text_left = Text(str(number1), font_size=24, color=text_color_left)
    number_text_right = Text(str(number2), font_size=24, color=text_color_right)
    number_text_left.align_to(box, UL).shift(DOWN * 0.1 + RIGHT * 0.1)
    number_text_right.align_to(box, UR).shift(DOWN * 0.1 + LEFT * 0.1)

    result.add(box, number_text_left, number_text_right)
    return result

def createCustomDoubledMatrix(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 8, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix0(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 8, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix1(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 8, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix2(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 8, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix3(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 8, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix4(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 8, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 2, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix5(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 8, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 5, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix6(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(1, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(0, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 8, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledMatrix7(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(2, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(0, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 8, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 7, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 2, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomeMatrixFINAL0(textColor):
    
    matrix = VGroup()
    box_list = []
    
    box_list.append(createTextbox333(15, textColor))
    box_list.append(createTextbox333(18, textColor))
    box_list.append(createTextbox333(21, textColor))
    box_list.append(createTextbox333(42, textColor))
    box_list.append(createTextbox333(54, textColor))
    box_list.append(createTextbox333(66, textColor))
    box_list.append(createTextbox333(69, textColor))
    box_list.append(createTextbox333(90, textColor))
    box_list.append(createTextbox333(111, textColor))

    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=0.25)
    return matrix





class Cannon(Scene):
    def construct(self):
        
        matrixA = createMatrix(WHITE)
        matrixB = createMatrix(YELLOW)
        matrixC = createBlankMatrix()

        # Create multiplication and equal signs
        times_sign = MathTex("\\times")
        equals_sign = MathTex("=")

        # Group the matrices and the signs
        matrices_with_signs = VGroup(
            matrixA, times_sign, matrixB, equals_sign, matrixC
        ).arrange(RIGHT, buff=0.5)

        

        # Center the entire group on the screen
        matrices_with_signs.move_to(ORIGIN)

        # Add the group to the scene
        self.add(matrices_with_signs)
        self.wait(4)
        

        # Fade out matrixC, times_sign, and equals_sign
        self.play(
            
            FadeOut(times_sign),
            FadeOut(equals_sign)
        )

        

        self.wait()




        

        animations = []
        for i in range(9):
            number_text = matrixA[i][1]
            box_center = matrixC[i].get_center()
            offset = np.array([-0.32, 0.28, 0])  # pos in box
            target_position = box_center + offset
            animations.append(number_text.animate.move_to(target_position))
            
            number_text = matrixB[i][1]
            box_center = matrixC[i].get_center()
            offset = np.array([0.32, 0.28, 0])  # pos in box
            target_position = box_center + offset
            animations.append(number_text.animate.move_to(target_position))

        
        self.play(*animations)
        
        '''
        self.play(
            FadeOut(matrixA, matrixB)

        )

        self.wait(2)
        '''
        

        realMatrixC = createCustomDoubledMatrix(YELLOW, WHITE, 0.25)
        self.play(
            FadeOut(matrixA, matrixB, matrixC),
            FadeIn(realMatrixC.shift(RIGHT * 4.79))
        )

        
        self.wait()

        self.play(
            realMatrixC.animate.move_to(ORIGIN)
        )
        self.wait()
        
        

        

        # Define arc path for the first movement sequence in top_left_animations
        arcPath0 = ArcBetweenPoints(realMatrixC[3][1].get_center(), realMatrixC[5][1].get_center(), angle=PI/2)
        
        top_left_animations = [
            MoveAlongPath(realMatrixC[3][1], arcPath0),
            realMatrixC[4][1].animate.move_to(realMatrixC[3][1]),
            realMatrixC[5][1].animate.move_to(realMatrixC[4][1]),
            
        ]
#############################################################################
        self.play(*top_left_animations,
                  run_time=1)
        
        stepZero1 = createCustomDoubledMatrix0(YELLOW, WHITE, 0.25)
        self.play(
            FadeOut(realMatrixC),
            FadeIn(stepZero1),
            run_time = 0.00000000000000001
        )
        
        
        

        # Define arc path for the first movement sequence in top_left_animations2
        arcPath1 = ArcBetweenPoints(stepZero1[6][1].get_center(), stepZero1[8][1].get_center(), angle=PI/2)
        
        top_left_animations2 = [
            MoveAlongPath(stepZero1[6][1], arcPath1),
            stepZero1[7][1].animate.move_to(stepZero1[6][1]),
            stepZero1[8][1].animate.move_to(stepZero1[7][1]),
        ]

        self.play(*top_left_animations2)
        
        stepZero2 = createCustomDoubledMatrix1(YELLOW, WHITE, 0.25)
        self.play(
            FadeOut(stepZero1),
            FadeIn(stepZero2),
            run_time = 0.00000000000000001
        )
        

        # Define arc path for the first movement sequence in top_left_animations3
        arcPath2 = ArcBetweenPoints(stepZero2[6][1].get_center(), stepZero2[8][1].get_center(), angle=PI/2)
        
        top_left_animations3 = [
            MoveAlongPath(stepZero2[6][1], arcPath2),
            stepZero2[7][1].animate.move_to(stepZero2[6][1]),
            stepZero2[8][1].animate.move_to(stepZero2[7][1]),
        ]

        self.play(*top_left_animations3)
        
        
        stepZero3 = createCustomDoubledMatrix2(YELLOW, WHITE, 0.25)
        self.play(
            FadeOut(stepZero2),
            FadeIn(stepZero3),
            run_time = 0.00000000000000001
        )

        # Define arc path for the first movement sequence in realTopLeftAnimations
        arcPath3 = ArcBetweenPoints(stepZero3[1][2].get_center(), stepZero2[7][2].get_center(), angle=PI/2)
        
        realTopLeftAnimations = [
            MoveAlongPath(stepZero3[1][2], arcPath3),
            stepZero3[4][2].animate.move_to(stepZero2[1][2]),
            stepZero3[7][2].animate.move_to(stepZero2[4][2]),
        ]
        
        self.play(*realTopLeftAnimations)
        
        stepZero4 = createCustomDoubledMatrix3(YELLOW, WHITE, 0.25)
        self.play(
            FadeOut(stepZero3),
            FadeIn(stepZero4),
            run_time = 0.00000000000000001
        )

        # Define arc path for the first movement sequence in realTopLeftAnimations2
        arcPath4 = ArcBetweenPoints(stepZero4[2][2].get_center(), stepZero4[8][2].get_center(), angle=PI/2)
        
        realTopLeftAnimations2 = [
            MoveAlongPath(stepZero4[2][2], arcPath4),
            stepZero4[5][2].animate.move_to(stepZero4[2][2]),
            stepZero4[8][2].animate.move_to(stepZero4[5][2]),
        ]
        
        self.play(*realTopLeftAnimations2)
        
        stepZero5 = createCustomDoubledMatrix4(YELLOW, WHITE, 0.25)
        self.play(
            FadeOut(stepZero4),
            FadeIn(stepZero5),
            run_time = 0.00000000000000001
        )

        # Define arc path for the first movement sequence in realTopLeftAnimations3
        arcPath5 = ArcBetweenPoints(stepZero5[2][2].get_center(), stepZero5[8][2].get_center(), angle=PI/2)
        
        realTopLeftAnimations3 = [
            MoveAlongPath(stepZero5[2][2], arcPath5),
            stepZero5[5][2].animate.move_to(stepZero5[2][2]),
            stepZero5[8][2].animate.move_to(stepZero5[5][2]),
        ]
        
        self.play(*realTopLeftAnimations3)
        
        stepZero6 = createCustomDoubledMatrix5(YELLOW, WHITE, .25)
        self.play(
            FadeOut(stepZero5),
            FadeIn(stepZero6),
            run_time = 0.00000000000000001
        )
    
        def addProductToBoxesWithFade(matrix):
            fade_in_animations = []
            fade_out_animations = []
            for box in matrix:
                number1 = int(box[1].text)
                number2 = int(box[2].text)
                product = number1 * number2
                
                # Create the multiplication sign text
                multiplication_sign = MathTex(r'\boldsymbol{\times}', font_size=30, color=BLACK)


                multiplication_sign.move_to(box[1].get_center()).shift(RIGHT * 0.333333)              
                # Create the product tex
                product_text = Text(str(product), font_size=24, color=BLACK)
                product_text.align_to(box[0], DR).shift(UP * 0.1 + LEFT * 0.1)
                
                # Add texts to the box
                box.add(multiplication_sign, product_text)
                
                # Create fade-in and fade-out animations
                fade_in_animations.append(FadeIn(multiplication_sign))
                fade_in_animations.append(FadeIn(product_text))
                fade_out_animations.append(FadeOut(multiplication_sign))
                fade_out_animations.append(FadeOut(product_text))
            
            return fade_in_animations, fade_out_animations



        fade_in_animations, fade_out_animations = addProductToBoxesWithFade(stepZero6)
        self.play(*fade_in_animations)
        self.wait(1)  # Pause for a second
        self.play(*fade_out_animations)
        self.wait()

        arcPath6 = ArcBetweenPoints(stepZero6[0][1].get_center(), stepZero6[2][1].get_center(), angle=PI/2)
        arcPath7 = ArcBetweenPoints(stepZero6[3][1].get_center(), stepZero6[5][1].get_center(), angle=PI/2)
        arcPath8 = ArcBetweenPoints(stepZero6[6][1].get_center(), stepZero6[8][1].get_center(), angle=PI/2)

        
        nextAnimation = [
            MoveAlongPath(stepZero6[0][1], arcPath6),
            stepZero6[1][1].animate.move_to(stepZero6[0][1]),
            stepZero6[2][1].animate.move_to(stepZero6[1][1]),
            MoveAlongPath(stepZero6[3][1], arcPath7),
            stepZero6[4][1].animate.move_to(stepZero6[3][1]),
            stepZero6[5][1].animate.move_to(stepZero6[4][1]),
            MoveAlongPath(stepZero6[6][1], arcPath8),
            stepZero6[7][1].animate.move_to(stepZero6[6][1]),
            stepZero6[8][1].animate.move_to(stepZero6[7][1]),
        ]
        self.play(*nextAnimation)
        
        arcPath6 = ArcBetweenPoints(stepZero6[0][2].get_center(), stepZero6[6][2].get_center(), angle=PI/2)
        arcPath7 = ArcBetweenPoints(stepZero6[1][2].get_center(), stepZero6[7][2].get_center(), angle=PI/2)
        arcPath8 = ArcBetweenPoints(stepZero6[2][2].get_center(), stepZero6[8][2].get_center(), angle=PI/2)

        nextAnimation2 = [
            MoveAlongPath(stepZero6[0][2], arcPath6), #
            stepZero6[3][2].animate.move_to(stepZero6[0][2]),
            stepZero6[6][2].animate.move_to(stepZero6[3][2]),
            MoveAlongPath(stepZero6[1][2], arcPath7), #
            stepZero6[4][2].animate.move_to(stepZero6[1][2]),
            stepZero6[7][2].animate.move_to(stepZero6[4][2]),
            MoveAlongPath(stepZero6[2][2], arcPath8), #
            stepZero6[5][2].animate.move_to(stepZero6[2][2]),
            stepZero6[8][2].animate.move_to(stepZero6[5][2]),
        ]
        self.play(*nextAnimation2)
        self.wait()
        stepZero6.set_opacity(0)

        nextStep = createCustomDoubledMatrix6(YELLOW, WHITE, 0.25)
        self.add(nextStep)

        def addProductToBoxesWithFade2(matrix):
            fade_in_animations = []
            fade_out_animations = []
            
            # Hardcoded values to add to the product for each box
            add_values = [0, 4, 16, 12, 35, 6, 48, 6, 35]  # Example: squares of 0 through 8

            for i, box in enumerate(matrix):
                if i >= len(add_values):
                    raise IndexError("Not enough hardcoded values for the number of boxes in matrix.")

                number1 = int(box[1].text)
                number2 = int(box[2].text)
                product = number1 * number2
                
                # Add the corresponding value from add_values to the product
                product += add_values[i]
                
                # Create the multiplication sign text
                multiplication_sign = MathTex(r'\boldsymbol{\times}', font_size=35, color=BLACK)
                multiplication_sign.move_to(box[1].get_center()).shift(RIGHT * 0.333333)
                
                # Create the product text
                product_text = Text(str(product), font_size=24, color=BLACK)
                product_text.align_to(box[0], DR).shift(UP * 0.1 + LEFT * 0.1)
                
                # Add texts to the box
                box.add(multiplication_sign, product_text)
                
                # Create fade-in and fade-out animations
                fade_in_animations.append(FadeIn(multiplication_sign))
                fade_in_animations.append(FadeIn(product_text))
                fade_out_animations.append(FadeOut(multiplication_sign))
                fade_out_animations.append(FadeOut(product_text))
            
            return fade_in_animations, fade_out_animations



        fade_in_animations, fade_out_animations = addProductToBoxesWithFade2(nextStep)
        self.play(*fade_in_animations)
        self.wait()  # Pause for a second
        self.play(*fade_out_animations)
        self.wait()
        
        
        
        

        arcPath6 = ArcBetweenPoints(nextStep[0][1].get_center(), nextStep[2][1].get_center(), angle=PI/2)
        arcPath7 = ArcBetweenPoints(nextStep[3][1].get_center(), nextStep[5][1].get_center(), angle=PI/2)
        arcPath8 = ArcBetweenPoints(nextStep[6][1].get_center(), nextStep[8][1].get_center(), angle=PI/2)

        nextAnimation = [
            MoveAlongPath(nextStep[0][1], arcPath6),
            nextStep[1][1].animate.move_to(nextStep[0][1]),
            nextStep[2][1].animate.move_to(nextStep[1][1]),
            MoveAlongPath(nextStep[3][1], arcPath7),
            nextStep[4][1].animate.move_to(nextStep[3][1]),
            nextStep[5][1].animate.move_to(nextStep[4][1]),
            MoveAlongPath(nextStep[6][1], arcPath8),
            nextStep[7][1].animate.move_to(nextStep[6][1]),
            nextStep[8][1].animate.move_to(nextStep[7][1]),
        ]
        self.play(*nextAnimation)

        arcPath6 = ArcBetweenPoints(nextStep[0][2].get_center(), nextStep[6][2].get_center(), angle=PI/2)
        arcPath7 = ArcBetweenPoints(nextStep[1][2].get_center(), nextStep[7][2].get_center(), angle=PI/2)
        arcPath8 = ArcBetweenPoints(nextStep[2][2].get_center(), nextStep[8][2].get_center(), angle=PI/2)

        nextAnimation2 = [
            MoveAlongPath(nextStep[0][2], arcPath6), #
            nextStep[3][2].animate.move_to(nextStep[0][2]),
            nextStep[6][2].animate.move_to(nextStep[3][2]),
            MoveAlongPath(nextStep[1][2], arcPath7), #
            nextStep[4][2].animate.move_to(nextStep[1][2]),
            nextStep[7][2].animate.move_to(nextStep[4][2]),
            MoveAlongPath(nextStep[2][2], arcPath8), #
            nextStep[5][2].animate.move_to(nextStep[2][2]),
            nextStep[8][2].animate.move_to(nextStep[5][2]),
        ]
        self.play(*nextAnimation2)
        nextStep.set_opacity(0)
        nextStep2 = createCustomDoubledMatrix7(YELLOW, WHITE, 0.25)
        self.add(nextStep2)
        self.wait()

        def addProductToBoxesWithFade3(matrix):
            fade_in_animations = []
            fade_out_animations = []
            endProducts = []
            
            # Hardcoded values to add to the product for each box
            add_values = [3, 18, 16, 42, 38, 26, 48, 34, 99]  # Example: squares of 0 through 8

            for i, box in enumerate(matrix):
                if i >= len(add_values):
                    raise IndexError("Not enough hardcoded values for the number of boxes in matrix.")

                number1 = int(box[1].text)
                number2 = int(box[2].text)
                product = number1 * number2
                
                # Add the corresponding value from add_values to the product
                product += add_values[i]
                
                
                # Create the multiplication sign text
                multiplication_sign = MathTex(r'\boldsymbol{\times}', font_size=35, color=BLACK)
                multiplication_sign.move_to(box[1].get_center()).shift(RIGHT * 0.333333)
                
                # Create the product text
                product_text = Text(str(product), font_size=24, color=BLACK)
                product_text.align_to(box[0], DR).shift(UP * 0.1 + LEFT * 0.1)
                
                # Add texts to the box
                box.add(multiplication_sign, product_text)
                
                # Create fade-in and fade-out animations
                fade_in_animations.append(FadeIn(multiplication_sign))
                fade_in_animations.append(FadeIn(product_text))
                fade_out_animations.append(FadeOut(multiplication_sign))
                #fade_out_animations.append(FadeOut(product_text))
                #fade_out_animations.append(product_text.animate.move_to(UP * 0.33333 + RIGHT * 0.3333))
            
            return fade_in_animations, fade_out_animations        

        
        fade_in_animations, fade_out_animations = addProductToBoxesWithFade3(nextStep2)


        self.play(*fade_in_animations)
        self.wait()  # Pause for a second
        #make the numbers in the bottom right (from addProductToBoxesWithFade3) move to the center while the numbers in the top left and bottom right fade out
        fadeoutLast = []

        for i in range(9):
            fadeoutLast.append(FadeOut(nextStep2[i][1]))
            fadeoutLast.append(FadeOut(nextStep2[i][2]))
            
        
        self.play(fadeoutLast, fade_out_animations)
        
        newnew = createCustomeMatrixFINAL0(BLACK)
        nextStep2.set_opacity(0)
        self.add(newnew)
        lastanimation = []
        
        
        
        
        for i in range(9):
            lastanimation.append(newnew[i][1].animate.move_to(newnew[i]))
        self.play(lastanimation)
        
        self.play(
            newnew.animate.move_to(matrixC)
        )
        
        matrixA1 = createMatrix(WHITE)
        matrixB1 = createMatrix(YELLOW)
        matrixC1 = createMatrix(PINK) # dud for centering

        matrixC1.set_opacity(0)
        # Create multiplication and equal signs
        times_sign1 = MathTex("\\times")
        equals_sign1 = MathTex("=")

        # Group the matrices and the signs
        matrices_with_signs1 = VGroup(
            matrixA1, times_sign1, matrixB1, equals_sign1, matrixC1
        ).arrange(RIGHT, buff=0.5)
        matrices_with_signs1.move_to(ORIGIN)
        self.play(FadeIn(matrices_with_signs1))
        self.wait(5)


        