class Depositos{
    const formacionesArmadas = []
    const locomotorasSueltas = []
    
    method vagonesMasPesadosDeFormaciones() = formacionesArmadas.map({f=> f.vagonMasPesado()})
    
    method necesitaConductorExperimentado()=
        formacionesArmadas.any({f => f.esCompleja()})
        
    method agregarLocomotoraAFormacion(unaFormacion) {
        if(!unaFormacion.puedeMoverse()){

            self.agregarLocomotoraA(unaFormacion)
        
        }
    }
    method agregarLocomotoraA(unaFormacion) {
        if(self.hayLocomotoraUtil(unaFormacion)){
            const locomotoraUtil = self.hallarLocomotoraUtil(unaFormacion)
            unaFormacion.agregarLocomotoras(locomotoraUtil)
            locomotorasSueltas.remove(locomotoraUtil)

        }
    }
    method hallarLocomotoraUtil(unaFormacion){
        return locomotorasSueltas.find({l => l.fuerzaDeArrastre() >= unaFormacion.empujeFaltante()})
    }
    method hayLocomotoraUtil(unaFormacion){
        return locomotorasSueltas.any({l => l.fuerzaDeArrastre() >= unaFormacion.empujeFaltante()})
    }
}




