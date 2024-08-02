from manim import *

def create_textbox(number, position, text_color):
    result = VGroup()  # create a VGroup
    box = Rectangle(  # create a box
        height=1, width=1, fill_color=BLUE, 
        fill_opacity=0.5, stroke_color=BLUE
    )
    
    number_text = Text(str(number), font_size=24, color=text_color)
    
    if position == "top_left":
        number_text.align_to(box, UL).shift(DOWN * 0.1 + RIGHT * 0.1)
    elif position == "bottom_right":
        number_text.align_to(box, DR).shift(UP * 0.1 + LEFT * 0.1)
    
    result.add(box, number_text)  # add both objects to the VGroup
    return result

def create_matrix(position, text_color):
    matrix = VGroup()
    box_list = []
    for i in range(9):
        box_list.append(create_textbox(i, position, text_color))
    matrix.add(*box_list)  # add the elements of box_list to the matrix
    matrix.arrange_in_grid(rows=3, cols=3, buff=0)
    
    return matrix

def createDoubledTextbox(number, text_color_right, text_color_left):
    result = VGroup()
    box = Rectangle(
        height=1, width=1, fill_color=BLUE,
        fill_opacity=0.5, stroke_color=BLUE
    )
    number_text_left = Text(str(number), font_size=24, color=text_color_left)
    number_text_right = Text(str(number), font_size=24, color=text_color_right)
    number_text_right.align_to(box, UL).shift(DOWN * 0.1 + RIGHT * 0.1)
    number_text_left.align_to(box, DR).shift(UP * 0.1 + LEFT * 0.1)

    result.add(box, number_text_left, number_text_right)
    return result

def createDoubledMatrix(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    for i in range (9):
        box_list.append(createDoubledTextbox(i, textColor1, textColor2))
        
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

def createCustomDoubledTextbox(number1, number2, text_color_right, text_color_left):
    result = VGroup()
    box = Rectangle(
        height=1, width=1, fill_color=BLUE,
        fill_opacity=0.5, stroke_color=BLUE
    )
    number_text_left = Text(str(number1), font_size=24, color=text_color_left)
    number_text_right = Text(str(number2), font_size=24, color=text_color_right)
    number_text_right.align_to(box, UL).shift(DOWN * 0.1 + RIGHT * 0.1)
    number_text_left.align_to(box, DR).shift(UP * 0.1 + LEFT * 0.1)

    result.add(box, number_text_left, number_text_right)
    return result

def createCustomDoubledMatrix(textColor1, textColor2, buffer):
    matrix = VGroup()

    box_list = []
    
    box_list.append(createCustomDoubledTextbox(0, 0, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(1, 1, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(2, 2, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(4, 4, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(5, 5, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(3, 3, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(8, 8, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(6, 6, textColor1, textColor2))
    box_list.append(createCustomDoubledTextbox(7, 7, textColor1, textColor2))
    matrix.add(*box_list)
    matrix.arrange_in_grid(rows=3, cols=3, buff=buffer)
    return matrix

class TextBox(Scene):
    def construct(self):
        
        
        # Create first matrix
        matrix1 = create_matrix("top_left", WHITE)
        
        # Create second matrix
        matrix2 = create_matrix("bottom_right", BLACK)
        
        # Ensure matrix2 is in front of matrix1 by setting z_index
        
        
        # Group the matrices together
        matrices = VGroup(matrix1, matrix2).arrange(RIGHT, buff=5)
        matrices.move_to(ORIGIN)
        
        # Create labels for the matrices
        label_a = Text("Matrix A", font_size=24).next_to(matrix1, UP)
        label_b = Text("Matrix B", font_size=24).next_to(matrix2, UP)
        
        # Add the group of matrices and labels to the scene
        self.add(matrices, label_a, label_b)
        
        # Wait for a few seconds before starting the fade out
        self.wait(3)
        
        # Create the fade out animation for the labels
        fade_out_labels = FadeOut(VGroup(label_a, label_b))
        
        # Play the fade out animation
        #self.play(fade_out_labels)
        
        self.wait()


        

        

        
        # Animate the buffer reduction
        self.play(
            matrices.animate.arrange(RIGHT, buff=-3),
            run_time=2
        )
        
        self.wait()
        
        # Remove the original matrices and add the doubled matrix
        self.remove(matrix1, matrix2)
        doublematrix = createDoubledMatrix(WHITE, GREEN, 0)
        self.add(doublematrix)
        
        # Create and add a label for the doubled matrix
        
        
        self.wait()

        doublematrix2 = createDoubledMatrix(BLACK, WHITE, 0.5)
        self.play(Transform(doublematrix, doublematrix2))
        self.wait()
        
        arc_path = ArcBetweenPoints(
            start=doublematrix[3].get_center(),
            end=doublematrix[3].get_center() + RIGHT * 3,
            angle=PI / 2  # Adjust the angle for the arch
        )

        # Animate the movement of specific textboxes in doublematrix
        self.play(
            MoveAlongPath(doublematrix[3], arc_path),
            doublematrix[4].animate.move_to(doublematrix[4].get_center() + LEFT * 1.5),
            doublematrix[5].animate.move_to(doublematrix[5].get_center() + LEFT * 1.5),
            run_time=2
        )

        
        arc_path2 = ArcBetweenPoints(
            start=doublematrix[6].get_center() + LEFT * 3,
            end=doublematrix[7].get_center(),
            angle=PI / 2  # Adjust the angle for the arc
        )

        arc_path3 = ArcBetweenPoints(
            start=doublematrix[7].get_center() + LEFT * 3,
            end=doublematrix[8].get_center(),
            angle=PI / 2  # Adjust the angle for the arc
        )
        #MoveAlongPath(doublematrix[6], arc_path2),
            #MoveAlongPath(doublematrix[7], arc_path3),
        self.play(
            doublematrix[6].animate.move_to(doublematrix[6].get_center() + LEFT * 3),
            doublematrix[7].animate.move_to(doublematrix[7].get_center() + LEFT * 3),
            doublematrix[8].animate.move_to(doublematrix[8].get_center() + LEFT * 3),
            run_time=1
        )

        self.play(
            MoveAlongPath(doublematrix[6], arc_path2),
            MoveAlongPath(doublematrix[7], arc_path3),
            run_time=1
        )
        self.wait()

        self.play(
    # Top row movements
    doublematrix[0].animate.shift(DOWN * 0.5 + RIGHT * 0.5),
    doublematrix[1].animate.shift(DOWN * 0.5),
    doublematrix[2].animate.shift(DOWN * 0.5 + LEFT * 0.5),

    # Middle row movements
    doublematrix[3].animate.shift(LEFT * 0.5),
    doublematrix[4].animate.shift(RIGHT * 0.5),
    # box 5 stays in place

    # Bottom row movements
    doublematrix[6].animate.shift(UP * 0.5),
    doublematrix[7].animate.shift(UP * 0.5 + LEFT * 0.5),
    doublematrix[8].animate.shift(UP * 0.5 + RIGHT * 0.5),
    run_time=2
)
        doublematrix3 = createCustomDoubledMatrix(BLACK, WHITE, 0)
        self.remove(doublematrix)
        self.add(doublematrix3)
        self.wait()
        self.play(
            doublematrix3[0].animate.shift(UP * 1.5),
            run_time=2
        )
        



        

        #doublematrix3 = createCustomDoubledMatrix(BLACK, WHITE, 0)
       # self.play(Transform(doublematrix, doublematrix3))
      #  self.wait()
   #   self.remove(matrix1, matrix2)
    #    doublematrix = createDoubledMatrix(WHITE, BLACK, 0)
     #   self.add(doublem


     #remove doublematrix title x
     #dont combine matrix a and b, just have their numbers populate a new matrix
     #dont blow up, keep buffer of 0.5
     #shifts need to be instant for the second row.
     #change so that the numbers are moving, not the boxes bc you will need to keep the product of the shifted numbers in the same box...






        
        



        
        
        
        

