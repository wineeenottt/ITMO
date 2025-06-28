package Move;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class FireBlast extends SpecialMove {
    static  Type TYPE = Type.FIRE;
    static  double POWER = 110;
    static  double ACCURACY = 85;

    public FireBlast() {
        super(TYPE, POWER, ACCURACY);
    }
    @Override
    protected String describe(){
        return "Применил Fire Blast ";
    }
    @Override
    protected void applyOppEffects(Pokemon p){
        // Проверяем вероятность поджигания
        if (Math.random() < 0.1)
            // Применяем эффект поджигания
            Effect.burn(p);
    }
}

