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


ip

```yaml
wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:
    gateway: 10.0.0.1
    subnet: 255.255.0.0
    static_ip: 10.0.12.20
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





substitutions:
  friendly_name: hz9
  dummy: dummy

esphome:
  name: heating-9
  friendly_name: heating-9

esp32:
  board: esp32dev
  framework:
    type: esp-idf

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "f5YvJmEwtfEGjWWQuaJP2XcoiMOKggHC8WSn3WHwte4="

ota:
  - platform: esphome
    password: "b2d6864b7aa666fcd1e80359aa19dcef"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  manual_ip:
    gateway: 10.0.0.1
    subnet: 255.255.0.0
    static_ip: 10.0.12.22

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Heating-9 Fallback Hotspot"
    password: "E0AN4LKr4LMk"

captive_portal:

time:
- platform: sntp
  id: sntp_time
  timezone: "Europe/Berlin"

one_wire:
  - platform: gpio
    pin: 17

sensor:
-   platform: dallas_temp
    name: ${friendly_name} Temperatur Vorlauf
    id: bat001_dallas_1
    update_interval: 15s
    address: 0x2a0000073c922928

-   platform: dallas_temp
    name: ${friendly_name} Temperatur Rücklauf
    id: bat001_dallas_2
    update_interval: 15s
    address: 0xec0000072abe7928

-   platform: dallas_temp
    name: ${friendly_name} Temperatur Extra
    id: bat001_dallas_3
    update_interval: 15s
    address: 0x9e0000073cc4d328

packages:
  heizung:
    url: https://github.com/cvstebut/heizung-automation
    files: [area_az.yaml, area_bad.yaml, area_sp.yaml, area_sz.yaml, area_tr.yaml]
    ref: main
    refresh: 1s
