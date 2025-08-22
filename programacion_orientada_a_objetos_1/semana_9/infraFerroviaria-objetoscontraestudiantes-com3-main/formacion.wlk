class Formacion{
    const formacionVagones = []
    const formacionLocomotoras = []

    method agregarLocomotora(unaLocomotora){
        formacionLocomotoras.add(unaLocomotora)
    }
    method agregarLocomotoras(locomotoras){
        formacionLocomotoras.addAll(locomotoras)
    }

    method agregarVagon(unVagon){
        formacionVagones.add(unVagon)
    }
    method agregarVagones(vagones){
        formacionVagones.addAll(vagones)
    }
    method cantMaximaPasajeros(){
        return formacionVagones.sum({vagon => vagon.cantidadPasajeros()})
    }
    method cantVagonesPopulares(){
        return formacionVagones.count({vagon => self.esPopular(vagon)})
    }
    method esPopular(unVagon){
        return unVagon.cantidadPasajeros() >= 50
    }
    method esFormacionCarguera(){
        return formacionVagones.all({vagon => vagon.cargaMaxima() >= 1000 })
    }

    method dispersionDePeso(){
        return self.vagonMasPesado().pesoMaximo() - self.vagonMasLiviano().pesoMaximo()
    }
    
    method vagonMasPesado(){
        return formacionVagones.max({vagon => vagon.pesoMaximo()})
    }

    method vagonMasLiviano(){
        return formacionVagones.min({vagon => vagon.pesoMaximo()})
    }

    method cantBanosFormacion(){
        return formacionVagones.count({vagon => vagon.tieneBanos()})
    }

    method hacerMantenimiento(){
        formacionVagones.forEach({vagon => vagon.hacerMantenimiento()})
    }

    method estaEquilibradoDePasajeros(){
        (self.vagonConMenorCantidadDePasajeros() - self.vagonConMayorCantidadDePasajeros() ) <= 20
    }
    method vagonesConPasajeros(){
        return formacionVagones.filter({v => self.vagonLlevaPasajeros(v)})
    }
    method vagonConMenorCantidadDePasajeros(){
        return self.vagonesConPasajeros().min({vagon => vagon.cantidadPasajeros()})
    }
    method vagonConMayorCantidadDePasajeros(){
        return self.vagonesConPasajeros().max({vagon => vagon.cantidadPasajeros()})
    }
    
    method vagonLlevaPasajeros(unVagon){
        return unVagon.cantidadPasajeros() > 0
    }

    method vagonesSinPasajeros(){
        return formacionVagones.filter({v => !self.vagonLlevaPasajeros(v)})
    }

    method estaOrganizada(){
        return formacionVagones == (self.vagonesConPasajeros().addAll(self.vagonesSinPasajeros()))
    }

    method velocidadMaxima(){
        formacionLocomotoras.min({l => l.velocidadMaxima()}).velocidadMaxima()
    }
    method locomotorasEficientes(){
        return formacionLocomotoras.all({f => f.esEficiente()})
    }
    method puedeMoverse(){
        return self.fuerzaDeArrastreTotal() >= self.pesoMaximoFormacion()
    }
    method pesoMaximoFormacion(){
        return self.pesoTotalDeVagones() + self.pesoTotalDeLocomotoras()
    }
    method pesoTotalDeVagones(){
        return formacionVagones.sum({v => v.pesoMaximo()})
    }
    method pesoTotalDeLocomotoras(){
        return formacionLocomotoras.sum({l => l.peso()})
    }
    method fuerzaDeArrastreTotal(){
        return formacionLocomotoras.sum({l => l.fuerzaDeArrastre()})
    }
    method empujeFaltante(){
        return 0.max(self.pesoMaximoFormacion() - self.fuerzaDeArrastreTotal() )
    }
    method esCompleja(){
        return self.formacionCompleta() > 8 || self.pesoMaximoFormacion() > 80000
    }
    method formacionCompleta(){
        return formacionLocomotoras.size() + formacionVagones.size()
    }


}

//asd = New Formacion(formacionVagones=[127368127])
