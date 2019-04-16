# DailyOralLanguage.py

from graphics import *


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
    rect = Rectangle(Point(60, 170), Point(260, 200)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(163, 185), "Misplaced Modifiers").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Add button objects - Pronoun Case
    rect = Rectangle(Point(60, 230), Point(260, 260)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(163, 245), "Pronoun Case").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Add button objects - Punctuation
    rect = Rectangle(Point(60, 290), Point(260, 320)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(160, 305), "Punctuation").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Add button objects - Subject/Verb Agreement
    rect = Rectangle(Point(60, 350), Point(260, 380)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(159, 365), "Subject/Verb Agreement").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    win.getMouse()
    win.close()

main()


def misplacedmodifiers():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language, Misplaced Modifiers", width=320, height=450)
    win.setBackground(color_rgb(204, 236,255))

    # Add text objects
    text = Text(Point(160,45), "Daily Oral Language")
    text.setSize(20)
    text.draw(win)

    text = Text(Point(160,90), "The category is:")
    text.setSize(12)
    text.setTextColor("red")
    text.setStyle("italic")
    text.draw(win)

    text = Text(Point(160,120), "Misplaced Modifiers")
    text.setSize(16)
    text.setStyle("italic")
    text.setStyle("bold")
    text.draw(win)

    text = Text(Point(160, 170), "This sentence contains at least one error\n in grammar or "
                                  "word usage. Click on the\n word that is the problem or part of the problem.")
    text.setSize(11)
    text.draw(win)

    # Import first sentence from .csv file into this location.
    dummyText = Text(Point(160, 250), "Lorem ipsum dolor sit amet, animal\n deleniti fabellas vis in, te mel modus\n "
                                  "singulis accusata.")
    # count = 0
    # If user clicks within sensitive area surrounding answer where correct answer lies:
    # change answer text to red
    # print("Correct", explanation for its correctness)
    # elif count <= 3
    # count = count + i
    # print("Try ", count)
    # else change answer text color to red
    # print(explanation for its correctness)
    dummyText.setTextColor("gray")
    dummyText.setSize(13)
    dummyText.draw(win)

    # Home button
    rect = Rectangle(Point(20, 410), Point(90, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(57, 425), "Home").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # Check button becomes sensitive area where number of tries is revealed
    # rect = Rectangle(Point(120, 410), Point(190, 440)).draw(win)
    # rect.setFill(color_rgb(28, 147, 215))
    #dtext = Text(Point(155, 425), "Check").draw(win)
    #dtext.setTextColor("white")
    #dtext.setStyle("bold")

    # Next button
    rect = Rectangle(Point(220, 410), Point(290, 440)).draw(win)
    rect.setFill(color_rgb(28, 147, 215))
    text = Text(Point(255, 425), "Next").draw(win)
    text.setTextColor("white")
    text.setStyle("bold")

    # If next button is clicked, import next sentence from .csv file.

    win.getMouse()
    win.close()


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


def punctuation():
    # Create graphics window
    win = GraphWin(title="Daily Oral Language, Punctuation", width=320, height=450)
    win.setBackground(color_rgb(204, 236, 255))

    # Add text objects
    text = Text(Point(160, 45), "Daily Oral Language")
    text.setSize(20)
    xtext.draw(win)

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


def inside(point, rectangle):
    # Is point inside rectangle?

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

while True:
    clickPoint = win.getMouse()

    if inside(clickPoint, (Point(60, 170), Point(260, 200))):
        text.setText("right")
    elif inside(clickPoint, (Point(60, 230), Point(260, 260))):
        text.setText("right")
    elif inside(clickPoint, (Point(60, 290), Point(260, 320))):
        text.setText("right")
    elif inside(clickPoint, (Point(60, 350), Point(260, 380))):
        text.setText("right")









