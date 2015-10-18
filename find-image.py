import autopy


if __name__ == '__main__':
    next_actions = autopy.bitmap.Bitmap.open('next-actions.png')
    current_screen = autopy.bitmap.capture_screen()

    current_screen.save('current-screen.png')

    position = current_screen.find_bitmap(next_actions)

    if position:
        autopy.mouse.smooth_move(*position)
        autopy.mouse.click()
    else:
        print('...can\'t see it :(')
