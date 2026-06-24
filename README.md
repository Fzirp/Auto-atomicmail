# Atomic Mail Hybrid Automation Bot

A robust Python-based Selenium automation script designed to capture, parse, and streamline the dynamic, multi-step registration flow of Atomic Mail. It automatically processes all input forms and handles advanced security gates using a hybrid execution design.

---

## 📌 Detailed Execution Flow (How It Works)

1. **Automated Credential Generation:** Upon launch, the script dynamically generates a randomized username and a policy-compliant secure password (guaranteeing mixed-case letters, digits, and special characters).

2. **Form Automation Phases:**
   * **Step 1 (Personal Info):** Automatically detects and populates the `First Name` and `Last Name` fields, then submits the first stage.
   * **Step 2 (Mail Address):** Fills the freshly generated unique username into the address field and proceeds.
   * **Step 3 (Security Setup):** Synchronizes and fills both the `Password` and `Confirm Password` fields simultaneously to prevent match errors, then submits.

3. **Smart Hybrid Captcha Intervention (Crucial Step):**
   * After submitting the password, the platform loads the **Seed Phrase / Recovery Key** screen where high-tier bot mitigation mechanics (`Arkose Labs / FunCaptcha`) are dynamically triggered.
   * Instead of crashing or timing out, the bot safely pauses execution, locks the browser session open, and transfers temporary control to **You**.
   * **Action Required:** You must look at the opened Chrome window, manually click the black **"Download & Proceed"** button, and complete the visual CAPTCHA challenge presented on screen.

4. **Real-Time Resumption & Session Completion:**
   * The script monitors the browser state in the background. The exact millisecond the CAPTCHA is successfully solved, the script detects the state change, completes the background hook, and shuts down the browser cleanly.

5. **Database Logging:**
   * The fully registered and verified account details are appended instantly into a local text database file named `accounts.txt`.

---

## 🛠️ Requirements & Technical Dependencies

The project relies on Selenium and an automated driver manager. You can see the package configurations inside `requirements.txt`.

To install dependencies, run:
```bash
pip install -r requirements.txt
