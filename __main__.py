from retry import retry
import pyautogui as p
import time
import os


BOOKMARK_MENU_PATH = 'imgs/book-menu.png'
BOOKMARK_PATH = 'imgs/book.png'
BOOKMARK_GROUP_PATH = 'imgs/start.png'

p.PAUSE = 0.3
TYPE_INTERVAL_DEFAULT = 0.05
MOUSE_MOVE_DURATION = 0.2

###############################################################################

def move_to_desktop(desktop_number):
    p.hotkey('winleft', str(desktop_number))

def call_menu(program_hint, type_interval=TYPE_INTERVAL_DEFAULT):
    p.hotkey('winleft', 'd')
    p.typewrite(program_hint, interval=type_interval)
    p.press('enter')

def bring_new_window_to_focus():
    p.hotkey('winleft', 'w')

def move_mouse_to_center():
    width, height = p.size()
    p.moveTo(width / 2, height / 2,
             duration=MOUSE_MOVE_DURATION, tween=p.easeInOutQuad)

def switch_to_spanish_keyboard():
    p.press('f10')

def wait(seconds):
    time.sleep(seconds)

###############################################################################

def firefox_open_bookmarks_menu(bmenu_target_path=BOOKMARK_MENU_PATH):
    '''Open bookmarks sidemenu, if not already open'''
    if p.locateOnScreen(bmenu_target_path, grayscale=True) is None:
        p.hotkey('ctrl', 'b')

def firefox_close_bookmarks_menu(bmenu_target_path=BOOKMARK_MENU_PATH):
    '''Open bookmarks sidemenu, if not already open'''
    if p.locateOnScreen(bmenu_target_path, grayscale=True) is not None:
        p.hotkey('ctrl', 'b')

def firefox_unfold_bookmarks(bookmarks_target_path=BOOKMARK_PATH):
    item_pos = p.locateCenterOnScreen(bookmarks_target_path, grayscale=True)
    if item_pos is None:
        # Assume it's already unfolded.
        return
    p.moveTo(*item_pos, duration=MOUSE_MOVE_DURATION)
    p.click()

@retry(tries=3)
def firefox_open_all_tabs_under_START_group(group_target_path=BOOKMARK_GROUP_PATH):
    item_pos = p.locateCenterOnScreen(group_target_path, grayscale=True)
    if item_pos is None:
        print('could find it... retry?')
        raise RuntimeError('couldn not find group manu item')
    p.moveTo(*item_pos, duration=MOUSE_MOVE_DURATION)
    p.rightClick()
    p.moveRel(10, 10, duration=MOUSE_MOVE_DURATION)
    p.click()

def firefox_focus_on_tab(tab_number):
    p.hotkey('alt', str(tab_number))

def firefox_close_tab(tab_number):
    firefox_focus_on_tab(tab_number)
    p.hotkey('ctrl', 'w')

###############################################################################

if __name__ == '__main__':
    # Change to the program's directory
    os.chdir(os.path.dirname(__file__))

    move_to_desktop(2)
    call_menu('firefox')
    wait(2)
    bring_new_window_to_focus()
    firefox_open_bookmarks_menu()
    firefox_unfold_bookmarks()
    firefox_open_all_tabs_under_START_group()
    wait(1)
    firefox_close_tab(1)
    firefox_focus_on_tab(1)
    firefox_close_bookmarks_menu()
    switch_to_spanish_keyboard()
    move_mouse_to_center()
