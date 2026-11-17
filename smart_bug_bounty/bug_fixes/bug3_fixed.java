import java.util.Arrays;

public class bug3_fixed {
    public static double averageRating(int[] ratings) {
        if (ratings == null || ratings.length == 0) {
            throw new IllegalArgumentException("ratings must not be empty");
        }

        // A long avoids integer overflow when summing large rating arrays.
        long total = 0;
        for (int rating : ratings) {
            total += rating;
        }
        // Explicit floating-point division retains fractional averages.
        return (double) total / ratings.length;
    }

    public static void main(String[] args) {
        int[] ratings = {4, 5};
        System.out.println("Ratings: " + Arrays.toString(ratings));
        System.out.println("Average: " + averageRating(ratings));
    }
}
