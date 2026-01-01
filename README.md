# JPG-Glitch-Maker
         █████ ██           █████ ██         █ ███                    █ ███     ███                                █                    █████   ██    ██              █                            
      ██████  ████ █     ██████  ████      █  ████  █               █  ████  █   ███     █        █              ██                  ██████  █████ █████            ██                             
     ██   █  █ ████     ██   █  █  ███    █  █  ████               █  █  ████     ██    ███      ██              ██                 ██   █  █  █████ █████          ██                             
    █    █  █   ██     █    █  █    ███  █  ██   ██               █  ██   ██      ██     █       ██              ██                █    █  █   █ ██  █ ██           ██                             
        █  █     █         █  █      ██ █  ███                   █  ███           ██           ████████          ██                    █  █    █     █              ██                 ███  ████   
       ██ ██              ██ ██      ████   ██                  ██   ██           ██   ███    ████████    ████   ██  ███              ██ ██    █     █       ████   ██  ███      ███    ████ ████ █
       ██ ██              ██ ██      ████   ██   ███            ██   ██   ███     ██    ███      ██      █ ███  ███ █ ███             ██ ██    █     █      █ ███  ███ █ ███    █ ███    ██   ████ 
     ████ ██            ████ ██      █ ██   ██  ████  █         ██   ██  ████  █  ██     ██      ██     █   ████ ███   ███            ██ ██    █     █     █   ████ ███   █    █   ███   ██        
    █ ███ ██           █ ███ ██     █  ██   ██ █  ████          ██   ██ █  ████   ██     ██      ██    ██        ██     ██            ██ ██    █     █    ██    ██  ██   █    ██    ███  ██        
       ██ ██              ██ ███████   ██   ███    ██  ████████ ██   ███    ██    ██     ██      ██    ██        ██     ██████████    ██ ██    █     ██   ██    ██  ██  █     ████████   ██        
       ██ ██              ██ ██████     ██  ██     █             ██  ██     █     ██     ██      ██    ██        ██     ██            █  ██    █     ██   ██    ██  ██ ██     ███████    ██        
       ██ ██              ██ ██          ██ █      █              ██ █      █     ██     ██      ██    ██        ██     ██               █     █      ██  ██    ██  ██████    ██         ██        
       ██ ██              ██ ██           ███     █                ███     █      ██     ██      ██    ███     █ ██     ██           ████      █      ██  ██    ██  ██  ███   ████    █  ███       
       █  █           █   ██ ██            ███████                  ███████       ███ █  ███ █    ██    ███████  ██     ██          █  █████           ██  █████ ██ ██   ███ █ ███████    ███      
   ██     █          ██   ██ ██              ███                      ███          ███    ███            █████    ██    ██         █     ██                 ███   ██ ██   ███   █████              
  ████   █          ███   █  █                                                                                          █          █                                                               
  █  █ ██            ███    █                                                                                          █            █                                                              
 █    ██              ██████                                                                                          █              ██                                                            
     █                 ███                                                                                           █                                                                             


Turn your photos into **glitchy fuckery** easily!  
This tool processes JPEG images, creates glitched copies, and leaves your originals intact.

---

## What it does

- Scans your **Pictures directory** (Windows default) for `.jpg` / `.jpeg` files  
- Creates glitched copies in a **`glitched` folder**  
- Supports **two glitch modes**:
  - `swap` – swaps bytes randomly in the image data  
  - `shift` – shifts chunks of bytes to create visual distortion  
- Allows **adjusting glitch intensity** (low, medium, high)  

---

## Usage

Run the script with Python:

```bash
python glitch.py --intensity medium --mode random --seed 123
