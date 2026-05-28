package example;
// Environment code for project almoxarifado
import jason.asSyntax.*;
import jason.environment.*;
import jason.asSyntax.parser.*;
import java.text.ParseException;
import java.util.logging.*;
import java.util.Random;

public class Env extends Environment {
    String sortearPeca() {
        Random gerador = new Random();
        int sorteado = gerador.nextInt(3);
        if (sorteado == 0) {
            return "peca(peq)";
        }
        if (sorteado == 1) {
            return "peca(med)";
        }
        if (sorteado == 2) {
            return "peca(grd)";
        }
        return "";
    }
    private Logger logger = Logger.getLogger("almoxarifado."+Env.class.getName());
    String peca_sorteada = "peca(grd)"; //sortearPeca();
    /** Called before the MAS execution with the args informed in .mas2j */
    @Override
    public void init(String[] args) {
        super.init(args);
        try {
            addPercept(ASSyntax.parseLiteral(peca_sorteada));
            addPercept(ASSyntax.parseLiteral("dia(quarta)"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    @Override
    public boolean executeAction(String agName, Structure action) {
        
        // Variável para controlar se a ação foi reconhecida e executada com sucesso
        boolean acaoExecutada = false;

        if (agName.equals("r1") && action.toString().equals("guardar(peq)")) { 
            logger.info(agName + " está guardando peça pequena....");
            acaoExecutada = true;

        } else if (agName.equals("r2") && action.toString().equals("guardar(med)")) {
            logger.info(agName + " está guardando peça média....");
            acaoExecutada = true;

        } else if (action.toString().equals("guardar(grd)")) { 
            // DESAFIO 1: Captura qualquer robô (r1 ou r2) que execute guardar(grd)
            logger.info(agName + " está guardando peça GRANDE....");
            acaoExecutada = true;
            
            // Remove a crença peca(grd) do ambiente imediatamente após guardá-la
            try {
                removePercept(ASSyntax.parseLiteral(peca_sorteada));  
                logger.info("A crença " + peca_sorteada + " foi removida do ambiente.");
            } catch (Exception e) {
                e.printStackTrace();
            }

        } else {
            logger.info("executing: "+action+", but not implemented!");
        }

        // Deixamos o bloco abaixo comentado ou limpo para não apagar a peça 
        // antes da hora em outras ações genéricas.
        try {
            // removePercept(ASSyntax.parseLiteral(peca_sorteada));  <- Removido daqui
            // peca_sorteada = sortearPeca();   
            // Thread.sleep(4000);
            // logger.info("uma nova peça está sendo colocada no almoxarifado....");
            // addPercept(ASSyntax.parseLiteral(peca_sorteada));                    
        } catch (Exception e) {
            e.printStackTrace();
        }
        return acaoExecutada; 
    }
    /** Called before the end of MAS execution */
    @Override
    public void stop() {
        super.stop();
    }
}