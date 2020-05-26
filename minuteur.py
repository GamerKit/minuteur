import time

seconde=0
minute=0
heure=0

continuer = True

while continuer == True:
    time.sleep(1)
    seconde=seconde+1
    print(heure, "h", minute, "min", seconde, "s")


    if seconde == 59:
        continuer = False
        seconde = 0
        continuer = True
        minute=minute+1

    if minute == 59:
        continuer = False
        seconde = 0
        minute = 0
        continuer = True
        heure=heure+1



