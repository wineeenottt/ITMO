public class lab1 {
    public static void main(String[] args) {

        int[] z = generateArrayZ();
        float[] x = generateMassiveX();

        double[][] c = new double[12][10];
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 10; j++) {
                double uks = x[j];

                switch (z[i]) {
                    case 10 -> c[i][j] = Math.pow((0.25 * Math.sin(Math.sin(uks))), 2);
                    case 2,6,14,18,22,24 -> c[i][j] = Math.log(Math.pow(Math.cos(2 * (2 - Math.pow(0.25 * (uks - (3.0 / 4.0)), 2))), 2));
                    default -> c[i][j] = Math.pow(Math.E, Math.cos(2 * Math.cos(uks)));
                }

                System.out.printf("%6.3f ", c[i][j]);
            }
            System.out.println();
        }
    }

    public static float[] generateMassiveX() {
        float[] x = new float[10];
        for (int i = 0; i < x.length; i++) {
            float max = 7.0f;
            float min = -14.0f;
            x[i] = min + (float) (Math.random() * (max - min));
        }
        return x;
    }

    public static int[] generateArrayZ(){
        int[] z = new int[12];
        for (int i = 0; i < z.length; i++) {
            z[i] = 2 + i * 2;
        }
        return z;
    }
}