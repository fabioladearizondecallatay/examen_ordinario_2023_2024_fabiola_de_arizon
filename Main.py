from Nave import EstrellaDeLaMuerte, NaveGrande, NavePequena

#instancias
estrella_muerte = EstrellaDeLaMuerte()
nave_pequena = NavePequena("Nave Pequeña 1")
nave_grande = NaveGrande("Nave Grande 1")

# Atacamos naves aliadas
estrella_muerte.atacar_nave_aliada(nave_pequena)
estrella_muerte.atacar_nave_aliada(nave_grande)