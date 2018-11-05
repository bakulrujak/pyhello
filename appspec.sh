version: 0.0
os: linux
files:
  - source: /
    destination: /opt
hooks:
  AfterInstall:
    - location: .scripts/initial.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: .scripts/start.sh
      timeout: 120
      runas: root