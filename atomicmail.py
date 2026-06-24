import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def generate_clean_string(length=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_digits(length=4):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))

# --- CONFIGURATION ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 12)

try:
    print("[+] Launching Atomic Mail Ultimate Registration Bot...")
    driver.get("https://atomicmail.io/app/auth/sign-up")
    
    # Credentials Generation
    first_name = "Amir"
    last_name = "Ali"
    username = "amir" + generate_clean_string(4) + generate_random_digits(3)
    password = "Secured" + generate_random_digits(4) + "!" + generate_clean_string(3).upper()
    
    print(f"[*] Target Account -> User: {username} | Pass: {password}")

    # ---- STEP 1: Personal Info ----
    print("[*] Processing Step 1: Names...")
    first_name_field = wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
    last_name_field = driver.find_element(By.NAME, "lastName")
    
    first_name_field.send_keys(first_name)
    time.sleep(0.3)
    last_name_field.send_keys(last_name)
    time.sleep(0.3)
    
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    print("[+] Step 1 submitted.")

    # ---- STEP 2: Mail Address ----
    print("[*] Processing Step 2: Choosing Mail Address...")
    mail_field = wait.until(EC.presence_of_element_located((
        By.XPATH, "//input[contains(@placeholder, 'alfie.hitchcock') or @type='text']"
    )))
    
    mail_field.send_keys(username)
    time.sleep(0.4)
    
    submit_button_2 = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button_2.click()
    print("[+] Step 2 submitted.")

    # ---- STEP 3: Password & Confirm Password ----
    print("[*] Processing Step 3: Entering Password & Confirm Password...")
    password_fields = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='password']")))
    
    password_fields[0].send_keys(password)
    time.sleep(0.4)
    password_fields[1].send_keys(password)
    time.sleep(0.4)
    
    final_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    final_submit.click()
    print("[+] Step 3 (Passwords) submitted.")

    # ---- STEP 4: Bulletproof Captcha Wait ----
    print("\n[!] CAPTCHA PAGE DETECTED!")
    print("[!] Please solve all captcha challenges manually in Chrome.")
    print("[*] Note: If Chrome closes too fast, we catch the log below.")
    
    # استفاده از یک ترفند مأموریتی: ربات به صورت پویا منتظر دکمه می‌ماند
    captcha_wait = WebDriverWait(driver, 180)
    
    # تلاش برای کلیک روی دکمه نهایی پس از اتمام کامل مراحل کپچا
    download_btn = captcha_wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[contains(text(), 'Download') or contains(., 'Download') or @type='button']"
    )))
    
    print("[+] Success trigger detected! Clicking Download & Proceed...")
    download_btn.click()

    # ---- SAVE TO FILE ----
    print("[*] Saving credentials to database file...")
    with open("accounts.txt", "a") as file:
        file.write(f"Email: {username}@atomicmail.io | Password: {password}\n")
    print("[+] Saved successfully inside 'accounts.txt'.")

    print("[*] Maintaining browser for 15 seconds to load dashboard...")
    time.sleep(15)

except Exception as e:
    print(f"\n[-] ERROR CAUGHT DURING CAPTCHA/SUBMIT: {e}")
    # اگر ارور داد، باز هم مانیتور را قفل نگه دار تا کروم بسته نشود و ببینی کجاست
    input("[?] Press ENTER in this terminal to close the browser manually...")

finally:
    driver.quit()
    print("[+] Browser closed. Automation session ended.")