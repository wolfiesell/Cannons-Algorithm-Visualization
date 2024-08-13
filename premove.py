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






class preCannon(Scene):
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
        self.wait(3)

        # Fade out matrixC, times_sign, and equals_sign
        self.play(
            
            FadeOut(times_sign),
            FadeOut(equals_sign)
        )

        

        self.wait(3)




        

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
        
        self.wait(2)
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


        


        