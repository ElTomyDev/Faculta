class VagonDeCarga{

    const property cargaMaxIdeal
    var property maderasSueltas
    method cargaMaxima() =
        cargaMaxIdeal - (400 * maderasSueltas)
    method pesoMaximo() = 
        1500 + self.cargaMaxima()
    method estaOrdenado(){}
    method cantidadPasajeros() = 0
    method hacerMantenimiento(){
        maderasSueltas = 0.max(maderasSueltas - 2)
    }
    method tieneBanos(){return false}
}