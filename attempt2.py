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

def createMatrix(textColor):
    matrix = VGroup()
    box_list = []
    for x in range(9):
        box_list.append(createTextbox(x, textColor))
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
    number_text_right.align_to(box, DR).shift(UP * 0.1 + LEFT * 0.1)

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




class Cannon(Scene):
    def construct(self):
        
        matrixA = createMatrix(WHITE)
        matrixB = createMatrix(YELLOW)
        matrixC = createBlankMatrix()

        matrices = VGroup(matrixA, matrixC, matrixB).arrange(RIGHT, buff = 1)
        matrices.move_to(ORIGIN)
        self.add(matrices)
        self.wait()
        

        animations = []
        for i in range(9):
            number_text = matrixA[i][1]
            box_center = matrixC[i].get_center()
            offset = np.array([-0.3, 0.3, 0])  # pos in box
            target_position = box_center + offset
            animations.append(number_text.animate.move_to(target_position))
            
            number_text = matrixB[i][1]
            box_center = matrixC[i].get_center()
            offset = np.array([0.3, -0.3, 0])  # pos in box
            target_position = box_center + offset
            animations.append(number_text.animate.move_to(target_position))

        
        self.play(*animations)
        
        
        realMatrixC = createCustomDoubledMatrix(YELLOW, WHITE, 0.25)
        self.remove(matrixC)
        self.add(realMatrixC)
        

        animations2 = []
        animations2.append(FadeOut(matrixA))
        animations2.append(FadeOut(matrixB))
        self.play(animations2)
        

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
        
        self.remove(realMatrixC)
        stepZero1 = createCustomDoubledMatrix0(YELLOW, WHITE, 0.25)
        self.add(stepZero1)

        # Define arc path for the first movement sequence in top_left_animations2
        arcPath1 = ArcBetweenPoints(stepZero1[6][1].get_center(), stepZero1[8][1].get_center(), angle=PI/2)
        
        top_left_animations2 = [
            MoveAlongPath(stepZero1[6][1], arcPath1),
            stepZero1[7][1].animate.move_to(stepZero1[6][1]),
            stepZero1[8][1].animate.move_to(stepZero1[7][1]),
        ]

        self.play(*top_left_animations2)
        
        stepZero2 = createCustomDoubledMatrix1(YELLOW, WHITE, 0.25)
        self.remove(stepZero1)
        self.add(stepZero2)
        

        # Define arc path for the first movement sequence in top_left_animations3
        arcPath2 = ArcBetweenPoints(stepZero2[6][1].get_center(), stepZero2[8][1].get_center(), angle=PI/2)
        
        top_left_animations3 = [
            MoveAlongPath(stepZero2[6][1], arcPath2),
            stepZero2[7][1].animate.move_to(stepZero2[6][1]),
            stepZero2[8][1].animate.move_to(stepZero2[7][1]),
        ]

        self.play(*top_left_animations3)
        
        self.remove(stepZero2)
        stepZero3 = createCustomDoubledMatrix2(YELLOW, WHITE, 0.25)
        self.add(stepZero3)

        # Define arc path for the first movement sequence in realTopLeftAnimations
        arcPath3 = ArcBetweenPoints(stepZero3[1][2].get_center(), stepZero2[7][2].get_center(), angle=PI/2)
        
        realTopLeftAnimations = [
            MoveAlongPath(stepZero3[1][2], arcPath3),
            stepZero3[4][2].animate.move_to(stepZero2[1][2]),
            stepZero3[7][2].animate.move_to(stepZero2[4][2]),
        ]
        
        self.play(*realTopLeftAnimations)
        self.remove(stepZero3)
        stepZero4 = createCustomDoubledMatrix3(YELLOW, WHITE, 0.25)
        self.add(stepZero4)

        # Define arc path for the first movement sequence in realTopLeftAnimations2
        arcPath4 = ArcBetweenPoints(stepZero4[2][2].get_center(), stepZero4[8][2].get_center(), angle=PI/2)
        
        realTopLeftAnimations2 = [
            MoveAlongPath(stepZero4[2][2], arcPath4),
            stepZero4[5][2].animate.move_to(stepZero4[2][2]),
            stepZero4[8][2].animate.move_to(stepZero4[5][2]),
        ]
        
        self.play(*realTopLeftAnimations2)
        
        self.remove(stepZero4)
        stepZero5 = createCustomDoubledMatrix4(YELLOW, WHITE, 0.25)
        self.add(stepZero5)

        # Define arc path for the first movement sequence in realTopLeftAnimations3
        arcPath5 = ArcBetweenPoints(stepZero5[2][2].get_center(), stepZero5[8][2].get_center(), angle=PI/2)
        
        realTopLeftAnimations3 = [
            MoveAlongPath(stepZero5[2][2], arcPath5),
            stepZero5[5][2].animate.move_to(stepZero5[2][2]),
            stepZero5[8][2].animate.move_to(stepZero5[5][2]),
        ]
        
        self.play(*realTopLeftAnimations3)
        self.remove(stepZero5)
        stepZero6 = createCustomDoubledMatrix5(YELLOW, WHITE, .25)
        self.add(stepZero6)
    
        def addProductToBoxesWithFade(matrix):
            fade_in_animations = []
            fade_out_animations = []
            for box in matrix:
                number1 = int(box[1].text)
                number2 = int(box[2].text)
                product = number1 * number2
                product_text = Text(str(product), font_size=24, color=RED)
                product_text.align_to(box[0], DL).shift(UP * 0.1 + RIGHT * 0.1)
                box.add(product_text)
                fade_in_animations.append(FadeIn(product_text))
                fade_out_animations.append(FadeOut(product_text))
            return fade_in_animations, fade_out_animations

        fade_in_animations, fade_out_animations = addProductToBoxesWithFade(stepZero6)
        self.play(*fade_in_animations)
        self.wait(1)  # Pause for a second
        self.play(*fade_out_animations)
        self.wait(3)

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
        nextStep = createCustomDoubledMatrix6(YELLOW, WHITE, 0.25)
        self.remove(stepZero6)
        self.add(nextStep)
        self.wait()

        fade_in_animations1, fade_out_animations2 = addProductToBoxesWithFade(nextStep)
        self.play(*fade_in_animations1)
        self.wait(1)  # Pause for a second
        self.play(*fade_out_animations2)
        self.wait()