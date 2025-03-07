heating-9

- Delete old device, if present
- Create New ESPHome device
- skip all steps until able to edit device yaml
- changes in yaml
  - ip
  - platform
    - esp-idf
  - time
  - substitutions
    - friendly_name: SHORTCODE (e.g. hz9)
  - ...
- save
- install / manually
- manually install firmware to device using esptool
- Test: Access logs wirelessly
- Test: Test wireless flashing with modification to dummy-substitution


heating-6
byRWJkA7hBl8ITXmhLqlvsrw+LpSfCEwZoFcuxETY+8=

ip
heating-9: 10.0.12.22
heating-6: 10.0.12.23

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:
    gateway: 10.0.0.1
    subnet: 255.255.0.0
    static_ip: 10.0.12.x
  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Heizung-Oben Fallback Hotspot"
    password: "redacted"
```

10.0.12.20   hz01   Heizung-Oben

f5YvJmEwtfEGjWWQuaJP2XcoiMOKggHC8WSn3WHwte4=


Install / Manual Download / "Factory format"

Move binary to esphome folder

```powershell
$com = "COM3"
$deviceName = "heating-9"
$targetFolder = "m:/data/projects/esphome/firmware"

mkdir $targetFolder
mv $env:USERPROFILE/downloads/${$devicename}.factory.bin $targetFolder
```

```powershell
# activate esphome venv
M:\data\projects\esphome\venv\Scripts\Activate.ps1
esptool --port $com write_flash 0x0  .\$($devicename).factory.bin
```
