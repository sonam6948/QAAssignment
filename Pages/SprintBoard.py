from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as W
from Config.config import TestData


class MainPage():

    """by locators - OR"""
    WAIT_TIME_OUT = TestData.WAIT_TIME_OUT
    EMAIL = TestData.EMAIL
    PASSWORD = TestData.PASSWORD
    BOARD_TITLE = TestData.BOARD_TITLE
    GREEN_BOARD_TITLE = TestData.GREEN_BOARD_TITLE
    GREEN_BOARD_DESC = TestData.GREEN_BOARD_DESC
    RED_BOARD_TITLE = TestData.RED_BOARD_TITLE

    """constructor"""
    def __init__(self, drv):
        self.drv = drv
        self.wait_variable = W(self.drv, self.WAIT_TIME_OUT)

    """login page"""
    def do_login(self):
        input_box_email = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        input_box_email.send_keys(self.EMAIL)
        input_box_password = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//input[@type='password']")))
        input_box_password.send_keys(self.PASSWORD)
        input_box_submit = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        input_box_submit.click()


    """Create Board"""
    def do_create_board(self):
        create_board_button = self.wait_variable.until(E.presence_of_element_located((By.LINK_TEXT, "Create Board")))
        create_board_button.click()
        title_box = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//input[@class='form-control']")))
        title_box.send_keys(self.BOARD_TITLE)
        assert "Create a Board – Sprint Boards" in  self.drv.title
        URL = self.drv.current_url
        assert "https://sprintboards.io/boards/create" in URL
        select_option = Select(
            self.wait_variable.until(E.presence_of_element_located((By.CLASS_NAME, "custom-select"))))
        select_option.select_by_visible_text("Sennder")
        submit_box = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit_box.click()
        URL_Boards = self.drv.current_url
        assert "https://sprintboards.io/boards" in URL_Boards

    """add green card"""
    def click_card_green(self):
        plus_button_green = self.wait_variable.until(E.presence_of_element_located((By.XPATH,
                                                                              "//*[@class='card m-1 p-0 btn align-items-center justify-content-center btn-link border-success empty-card text-success']")))
        plus_button_green.click()
        # Verify Add a  card text in dialog box
        addCardV = self.wait_variable.until(E.presence_of_element_located((By.ID, "add-card-modal")))
        assert "Add a Card" in addCardV.text

        green_card_title_input_box = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//input[@placeholder='Required']")))
        green_card_title_input_box.send_keys(self.GREEN_BOARD_TITLE)
        green_card_desc_input_box = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Optional']")))
        green_card_desc_input_box.send_keys(self.GREEN_BOARD_DESC)
        green_card_submit_button = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        green_card_submit_button.click()
        # Verify card is added with the mentioned title and description
        green_title_verify = self.wait_variable.until(E.presence_of_element_located((By.XPATH,
                                               "//body/div[@id='root']/div[@id='wrapper']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/h6[1]")))
        card_desc_green = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/div[1]/div/div/div/div/p")))
        assert self.GREEN_BOARD_TITLE in green_title_verify.text
        assert self.GREEN_BOARD_DESC in card_desc_green.text

        """add red card"""
    def click_card_red(self):
        plus_button_red = self.wait_variable.until(E.presence_of_element_located((By.XPATH,
                                                                                  "//*[@class='card m-1 p-0 btn align-items-center justify-content-center btn-link border-danger empty-card text-danger']")))
        plus_button_red.click()
        red_card_title_input_box = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//input[@placeholder='Required']")))
        red_card_title_input_box.send_keys(self.RED_BOARD_TITLE)
        red_card_submit_button = self.wait_variable.until(
            E.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        red_card_submit_button.click()

        # Verify card is added with the mentioned title and description
        card_title_red = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//*[@id='wrapper']/div/div[2]/div[1]/div[2]/div/div/div/h6")))
        card_desc_red = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//*[@class='text-secondary font-italic']")))
        assert self.RED_BOARD_TITLE in card_title_red.text
        assert "No description provided." in card_desc_red.text

    """click on thumps up logo for green card"""
    def click_thumps_up(self):
        thumps_up_button = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//button[@class='btn btn-link  text-muted mb-0 p-0']")))
        thumps_up_button.click()

    """delete the red card"""
    def click_delete_red_card(self):
        delete_button = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "(//button[@class='btn btn-link text-muted mb-0 p-0'])[4]")))
        delete_button.click()

        # Verify the text in  delete confirmation dialog box
        deleteboxtext = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//div[@class='modal-body']")))
        assert "Are you sure you want to continue?" in deleteboxtext.text

        confirm_button = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//*[@class='btn btn-danger']")))

        # Verify the text in  delete confirmation dialog box
        confirm_buttontext = self.wait_variable.until(E.presence_of_element_located((By.XPATH, "//*[@class='btn btn-danger']")))
        assert "Confirm" in confirm_buttontext.text

        confirm_button.click()