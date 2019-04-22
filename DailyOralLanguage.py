# DailyOralLanguage.py

from graphics import *
import time


def main():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language", width=320, height=450)
    win.setBackground(color_rgb(204, 236, 255))

    # Add text objects
    text = Text(Point(160, 45), "Daily Oral Language")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(160, 90), "Practice your English language skills\n"
                                 "by spotting the errors in these sentences.")
    text.setSize(11)
    text.draw(win)

    text = Text(Point(160, 140), "Select a category:")
    text.setSize(12)
    text.setTextColor("red")
    text.setStyle("italic")
    text.draw(win)

    # Add button objects - Misplaced Modifiers
    rect1 = Rectangle(Point(60, 170), Point(260, 200)).draw(win)
    rect1.setFill(color_rgb(28, 147, 215))
    text1 = Text(Point(163, 185), "Misplaced Modifiers").draw(win)
    text1.setTextColor("white")
    text1.setStyle("bold")

    # Add button objects - Pronoun Case
    rect2 = Rectangle(Point(60, 230), Point(260, 260)).draw(win)
    rect2.setFill(color_rgb(28, 147, 215))
    text2 = Text(Point(163, 245), "Pronoun Case").draw(win)
    text2.setTextColor("white")
    text2.setStyle("bold")

    # Add button objects - Punctuation
    rect3 = Rectangle(Point(60, 290), Point(260, 320)).draw(win)
    rect3.setFill(color_rgb(28, 147, 215))
    text3 = Text(Point(160, 305), "Punctuation").draw(win)
    text3.setTextColor("white")
    text3.setStyle("bold")

    # Add button objects - Subject/Verb Agreement
    rect4 = Rectangle(Point(60, 350), Point(260, 380)).draw(win)
    rect4.setFill(color_rgb(28, 147, 215))
    text4 = Text(Point(159, 365), "Subject/Verb Agreement").draw(win)
    text4.setTextColor("white")
    text4.setStyle("bold")


    while True:
        clickPoint = win.checkMouse()

        if clickPoint != None:

            if inside(clickPoint, rect1):
                misplacedmodifiers()
            elif inside(clickPoint, rect2):
                pronouncase()
            elif inside(clickPoint, rect3):
                punctuation()
            elif inside(clickPoint, rect4):
                # text4.setText("continuing . . .")
                subjectverbagreement()
            elif inside(clickPoint, rect5):
                main()
            elif inside(clickPoint, rect6):
                advancesentence()


def misplacedmodifiers():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language, Misplaced Modifiers", width=320, height=450)
    win.setBackground(color_rgb(204, 236,255))

    # Add text objects
    text = Text(Point(160,45), "Daily Oral Language")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(160,80), "The category is:")
    text.setSize(12)
    text.setTextColor("red")
    text.setStyle("italic")
    text.draw(win)

    text = Text(Point(160,110), "Misplaced Modifiers")
    text.setSize(16)
    text.setStyle("italic")
    text.setStyle("bold")
    text.draw(win)

    text = Text(Point(160, 190), "A misplaced modifier is a word or phrase\n"
                                 "that is supposed to describe something in\n"
                                 "the sentence. Modifiers need to be placed\n"
                                 "properly so that it is clear to the reader\n"
                                 "what is being described or modified. Click\n"
                                 "on the word below that is the problem or\n"
                                 "part of the problem.")
    text.setTextColor("black")
    text.setSize(11)
    text.draw(win)

    # Show sentence #1
    text = Text(Point(160, 290), "The teacher returned the exam to the\n student that was all marked up.")
    rectA = Rectangle(Point(105, 290), Point(275, 310)).draw(win)      # invisible rectangle around answer
    rectA.setOutline(color_rgb(204, 236, 255))                         # invisible rectangle around answer
    text.setTextColor("gray")
    text.setSize(13)
    text.draw(win)

    # Justification for correct answer
    # text = Text(Point(160, 340), "The teacher returned the exam that\n"
    #                              "was marked up to the student.")
    # text.setTextColor("red")
    # text.setSize(12)
    # text.setStyle("italic")
    # text.draw(win)

    # Home button
    rect5 = Rectangle(Point(20, 410), Point(90, 440)).draw(win)
    rect5.setFill(color_rgb(28, 147, 215))
    text5 = Text(Point(57, 425), "Home").draw(win)
    text5.setTextColor("white")
    text5.setStyle("bold")

    # Try again button
    # rect7 = Rectangle(Point(120, 410), Point(190, 440)).draw(win)
    # rect7.setOutline(color_rgb(204, 236, 255))
    # text7 = Text(Point(155, 425), "Try again").draw(win)
    # text7.setTextColor("red")
    # text7.setStyle("bold")

    # Next button
    rect6 = Rectangle(Point(220, 410), Point(290, 440)).draw(win)
    rect6.setFill(color_rgb(28, 147, 215))
    text6 = Text(Point(255, 425), "Next").draw(win)
    text6.setTextColor("white")
    text6.setStyle("bold")

    rectA2 = Rectangle(Point(113, 290), Point(265, 310)).draw(win)
    rectA2.setOutline(color_rgb(204, 236, 255))

    textcs = Text(Point(160, 340), "The teacher returned the exam that\n"
                                 "was marked up to the student.")

    textcs2 = Text(Point(160, 340), "On our kitchen table, we ate\n"
                                              "the meal our friends cooked.")


    # whichsentence = 0   # Use this if importing sentences from csv file
    while True:
        clickPoint = win.checkMouse()

        if clickPoint != None:

            if inside(clickPoint, rect5):
                main()

            # elif inside(clickPoint, rect6):
            #     whichsentence +=1
            #     advancesentence(text, whichsentence)



            elif inside(clickPoint, rectA):     # When user chooses the sensitized area holding answer 1
                rectA = Rectangle(Point(105, 290), Point(275, 310)).draw(win)      # invisible rectangle around answer
                rectA.setOutline(color_rgb(204, 236, 255))
                textc = Text(Point(155, 425), "Correct!").draw(win)
                textc.setTextColor("red")
                textc.setStyle("bold")
                time.sleep(1)
                textcs = Text(Point(160, 340), "The teacher returned the exam that\n"
                                 "was marked up to the student.")
                textcs.setTextColor("red")
                textcs.setSize(12)
                textcs.setStyle("italic")
                textcs.draw(win)
                time.sleep(2)
                rect = Rectangle(Point(10, 290), Point(300, 330))
                rect.setFill(color_rgb(204, 236, 255))
                rect.setOutline(color_rgb(204, 236, 255))
                time.sleep(2)
                textc.undraw()
                time.sleep(2)
                textcs.undraw()
                rectA.undraw()



            elif inside(clickPoint, rect6):     # Next button brings up sentence 2
                rect = Rectangle(Point(10, 260), Point(300, 360))#.draw(win)
                rect.setFill(color_rgb(204, 236, 255))
                rect.setOutline(color_rgb(204, 236, 255))
                rect.draw(win)
                text = Text(Point(160, 290), "We ate the meal our friends "
                                             "\ncooked on our kitchen table.")
                rectA2 = Rectangle(Point(113, 290), Point(265, 310)).draw(win)
                rectA2.setOutline(color_rgb(204, 236, 255))
                text.setTextColor("gray")
                text.setSize(13)
                text.draw(win)

            elif inside(clickPoint, rectA2) and question == 2:  # when user chooses the sensitized area holding answer 2
                textc = Text(Point(155, 425), "Correct!").draw(win)
                textc.setTextColor("red")
                textc.setStyle("bold")
                time.sleep(1)
                textcs2 = Text(Point(160, 340), "On our kitchen table, we ate\n"
                                              "the meal our friends cooked.")
                textcs2.setTextColor("red")
                textcs2.setSize(12)
                textcs2.setStyle("italic")
                textcs2.draw(win)
                time.sleep(2)
                rect = Rectangle(Point(10, 290), Point(300, 330))
                rect.setFill(color_rgb(204, 236, 255))
                rect.setOutline(color_rgb(204, 236, 255))
                time.sleep(2)
                textc.undraw()
                time.sleep(2)
                textcs2.undraw()


            elif clickPoint != inside(clickPoint, rectA):       # When user chooses incorrectly
                rect = Rectangle(Point(120, 410), Point(190, 440)).draw(win)
                rect.setOutline(color_rgb(204, 236, 255))
                textta = Text(Point(155, 425), "Try again").draw(win)
                textta.setTextColor("red")
                textta.setStyle("bold")
                time.sleep(1.5)
                textta.undraw()


    # win.getMouse()
    # win.close()


def pronouncase():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language, Pronoun Case", width=320, height=450)
    win.setBackground(color_rgb(204, 236, 255))

    # Add text objects
    text = Text(Point(160, 45), "Daily Oral Language")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(160, 90), "The category is:")
    text.setSize(12)
    text.setTextColor("red")
    text.setStyle("italic")
    text.draw(win)

    text = Text(Point(160, 120), "Pronoun Case")
    text.setSize(16)
    text.setStyle("italic")
    text.setStyle("bold")
    text.draw(win)

    text = Text(Point(160, 170), "This sentence contains at least one error\n in grammar or "
                                  "word usage. Click on the\n word that is the problem or part of the problem.")
    text.setSize(11)
    text.draw(win)

    dummyText = Text(Point(160, 250), "Me and Joe are going\n to the gym today.")
    dummyText.setTextColor("gray")
    dummyText.setSize(13)
    dummyText.draw(win)

    # Home button
    rect = Rectangle(Point(20, 410), Point(90, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(57, 425), "Home").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Next button
    rect = Rectangle(Point(220, 410), Point(290, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(255, 425), "Next").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    win.getMouse()
    win.close()


def punctuation():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language, Punctuation", width=320, height=450)
    win.setBackground(color_rgb(204, 236, 255))

    # Add text objects
    text = Text(Point(160, 45), "Daily Oral Language")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(160, 90), "The category is:")
    text.setSize(12)
    text.setTextColor("red")
    text.setStyle("italic")
    text.draw(win)

    text = Text(Point(160, 120), "Punctuation")
    text.setSize(16)
    text.setStyle("italic")
    text.setStyle("bold")
    text.draw(win)

    text = Text(Point(160, 170), "This sentence contains at least one error\n in grammar or "
                                  "word usage. Click on the\n word that is the problem or part of the problem.")
    text.setSize(11)
    text.draw(win)

    dummyText = Text(Point(160, 250), "Lorem ipsum dolor sit amet, animal\n deleniti fabellas vis in, te mel modus\n "
                                  "singulis accusata.")
    dummyText.setTextColor("gray")
    dummyText.setSize(13)
    dummyText.draw(win)

    # Home button
    rect = Rectangle(Point(20, 410), Point(90, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(57, 425), "Home").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Next button
    rect = Rectangle(Point(220, 410), Point(290, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(255, 425), "Next").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    win.getMouse()
    win.close()


def subjectverbagreement():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language, Subject/Verb Agreement", width=320, height=450)
    win.setBackground(color_rgb(204, 236, 255))

    # Add text objects
    text = Text(Point(160, 45), "Daily Oral Language")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(160, 90), "The category is:")
    text.setSize(12)
    text.setTextColor("red")
    text.setStyle("italic")
    text.draw(win)

    text = Text(Point(160, 120), "Subject/Verb Agreement")
    text.setSize(16)
    text.setStyle("italic")
    text.setStyle("bold")
    text.draw(win)

    text = Text(Point(160, 170), "This sentence contains at least one error\n in grammar or "
                                  "word usage. Click on the\n word that is the problem or part of the problem.")
    text.setSize(11)
    text.draw(win)

    dummyText = Text(Point(160, 250), "Lorem ipsum dolor sit amet, animal\n deleniti fabellas vis in, te mel modus\n "
                                  "singulis accusata.")
    dummyText.setTextColor("gray")
    dummyText.setSize(13)
    dummyText.draw(win)

    # Home button
    rect = Rectangle(Point(20, 410), Point(90, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(57, 425), "Home").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Next button
    rect = Rectangle(Point(220, 410), Point(290, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(255, 425), "Next").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    win.getMouse()
    win.close()


def advancesentence(text, index):
    infile = open('misplaced_modifiers.csv', 'r')
    data = infile.read()    # read all of the data
    lines = data.split('\n')    # split the data into sentences
    text.setText(lines[index])  # update the text object with the desired sentence


def inside(point, rectangle):
    # Is point inside rectangle?

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


if __name__ == "__main__":    # Lets the user import without running everything.
    main()









