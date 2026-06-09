# I installed Fedora Linux on my main machine and it was a wild ride. I wrote a madlibs generator to create a hilarious installation log.
# I has been one bothersome process with a lot of digging through forums, troubleshooting, and a few moments of sheer panic.
# The story is AI generated, but the experience is all real.
# I couldn't bother to write a whole story after the installation. It was tiresome.
# They make it look so easy in the YouTube videos, but in reality, it was a rollercoaster of emotions and technical challenges.
# I will stop yapping. Enjoy.

import time

def play_madlibs():
    print("======================================================")
    print(" 🐧 THE GREAT LINUX MIGRATION: THE SINGLE-BOOT CHRONICLES 🐧 ")
    print("======================================================")
    print("Fill in the blanks to generate your GitHub installation log...\n")

    cpu_brand = input("Your CPU Brand (e.g., AMD, Intel): ")
    gpu_model = input("Your GPU Model (e.g., RTX 5050, GTX 1650): ")
    distro = "Fedora"
    error_msg = input("A terrifying error message you saw (e.g., Kernel Module Missing): ")
    bios_key = input("The BIOS key you had to mash furiously (e.g., F2, F12): ")
    secret_pw = input("A ridiculous temporary BIOS password: ")
    game_site = "FitGirl-Repacks"
    cs_concept = input("A Computer Science concept that sounds fancy (e.g., Memory Leak, Multi-threading): ")
    victory_food = input("Your ultimate celebratory food (e.g., Pizza, Biryani): ")

    print("\n[!] Purging all traces of Windows...")
    time.sleep(1.5)
    print("[!] Reclaiming disk sectors for open-source dominance...")
    time.sleep(1)
    print("[!] Generating Markdown asset... \n")

    story = f"""
    ### THE LOG: How I Wiped My Drive and Found Salvation in {distro}

    It all started when I decided my {cpu_brand} processor deserved better than running Windows. 
    I didn't dual-boot. I didn't leave a safety net. I backed up nothing, flashed {distro} onto a thumb drive, 
    and nuked my entire drive into the stratosphere. "Windows is dead," I said. "I want to live on the edge."

    The initial boot was gorgeous—right up until the GNOME Software store encountered a minor 
    inconvenience and decided to spin its loading wheel until the heat death of the universe. 
    Naturally, as a sophisticated Computer Science student, I bypassed the entire GUI layout 
    using raw terminal commands, because clicking buttons is for the weak.

    But the universe demanded a sacrifice. Upon restarting, my screen flashed a glaring omen: 
    `"{error_msg}"`. My discrete {gpu_model} graphics card had entered a state of profound existential dread
    because the motherboard's Secure Boot security was acting like an overzealous bouncer.
    
    To fix it, I had to execute the ancient Acer ritual:
    1. Mash `{bios_key}` at startup like I was playing a competitive fighting game.
    2. Unlock the hidden BIOS settings by creating a highly classified supervisor password: `{secret_pw}`.
    3. Look Secure Boot dead in the eyes, toggle it to **Disabled**, and erase the final trace of corporate restriction.

    Once the hardware bouncer stopped blocking my custom-compiled kernel modules, {distro} snapped awake. 
    I fixed my broken screen brightness slider by forcing arguments directly into the GRUB bootloader, 
    mapped my local network to beam files to my phone using an 'Open With' hack that felt illegal, and prepared 
    my environment for the ultimate test: downloading compressed game files from {game_site} using a 
    Wine translation layer limited to 2GB of RAM to prevent a catastrophic `{cs_concept}` loop.

    Now, my custom keyboard shortcuts don't work, my terminal is named 'kgx' for reasons only the open-source 
    gods understand, and I am eating a glorious plate of {victory_food} in absolute triumph. 

    I am no longer a mere user. I am the sole ruler of this hardware. Everything is running perfectly, 
    and I am exactly one broken `sudo dnf update` away from absolute ruin. 

    **Status:** Fully Optimized. 🚀
    """

    print(story)

if __name__ == "__main__":
    play_madlibs()
