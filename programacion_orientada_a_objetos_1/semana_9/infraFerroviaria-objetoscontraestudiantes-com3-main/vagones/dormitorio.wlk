class VagonDormitorio {
    var property cantCompartimientos
    var property cantCamas

    var cantPasajeros = 5

    method initialize() {
        if (cantCompartimientos < 0 || cantCamas < 0){
            self.error("los valores deben ser positivos")
        }
    }

    method cantMaximaPasajeros() = cantCompartimientos * cantCamas
    method tieneBanos() = true
    method cargaMaxima() = 1200
    method pesoMaximo() = 4000 + (80*self.cantidadPasajeros()) + self.cargaMaxima()
    method cantidadPasajeros() = self.cantMaximaPasajeros()
    method hacerMantenimiento() {}
    
    
}