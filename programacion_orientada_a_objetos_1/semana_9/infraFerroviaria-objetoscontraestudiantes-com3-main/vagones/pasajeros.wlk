class VagonPasajeros {
    const property largo
    const property ancho
    const property tieneBanos
    var estaOrdenado = true

    method initialize() {
        if (largo < 0 || ancho < 0) {
            self.error("los valores deben ser positivos")
        }
    }

    
    
    method tieneBanos() = tieneBanos
    method estaOrdenado() = estaOrdenado

    method calcularPasajeros()= if (ancho < 3) largo * 8 else largo *10

    method cantidadPasajeros()=
        if(self.estaOrdenado()){
            self.calcularPasajeros()
        }else{ 
            self.calcularPasajeros() - 15
            }

    method cargaMaxima(){
        return  if(self.tieneBanos()){
                300
            }else{
                800
            }
        }

    method pesoMaximo()= 2000 + (self.cantidadPasajeros() * 80) + self.cargaMaxima()

    method hacerMantenimiento() {if (!self.estaOrdenado()) estaOrdenado = true}
}
