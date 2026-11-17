public class FixValidation {
    private static int passed = 0;

    private static void checkDouble(String label, double actual, double expected) {
        if (Math.abs(actual - expected) > 1e-12) {
            throw new AssertionError(label + ": expected " + expected + " got " + actual);
        }
        passed++;
        System.out.println("PASS " + label);
    }

    private static void checkInt(String label, int actual, int expected) {
        if (actual != expected) {
            throw new AssertionError(label + ": expected " + expected + " got " + actual);
        }
        passed++;
        System.out.println("PASS " + label);
    }

    private static void checkThrows(String label, Runnable action) {
        try {
            action.run();
        } catch (IllegalArgumentException expected) {
            passed++;
            System.out.println("PASS " + label);
            return;
        }
        throw new AssertionError(label + ": expected IllegalArgumentException");
    }

    public static void main(String[] args) {
        checkDouble("bug3 fractional average", bug3_fixed.averageRating(new int[]{4, 5}), 4.5);
        checkDouble("bug3 single rating", bug3_fixed.averageRating(new int[]{3}), 3.0);
        checkDouble("bug3 equal ratings", bug3_fixed.averageRating(new int[]{5, 5, 5}), 5.0);
        checkDouble("bug3 large ratings do not overflow", bug3_fixed.averageRating(new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE}), (double) Integer.MAX_VALUE);
        checkThrows("bug3 empty array rejected", () -> bug3_fixed.averageRating(new int[]{}));
        checkThrows("bug3 null array rejected", () -> bug3_fixed.averageRating(null));

        checkInt("bug6 all negatives", bug6_fixed.highestTemperature(new int[]{-7, -2, -5}), -2);
        checkInt("bug6 all positives", bug6_fixed.highestTemperature(new int[]{4, 8, 1}), 8);
        checkInt("bug6 mixed signs", bug6_fixed.highestTemperature(new int[]{-3, 0, 7}), 7);
        checkInt("bug6 single reading", bug6_fixed.highestTemperature(new int[]{-10}), -10);
        checkThrows("bug6 empty array rejected", () -> bug6_fixed.highestTemperature(new int[]{}));
        checkThrows("bug6 null array rejected", () -> bug6_fixed.highestTemperature(null));

        System.out.println("Java assertions passed: " + passed);
    }
}
