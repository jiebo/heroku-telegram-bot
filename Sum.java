
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

/**
 * Created by jiebo on 04/01/2018.
 */

public class Sum {
    public static void main(String[] args) {
        List<ArrayList> inputList = new ArrayList<ArrayList>();
        HashMap<Integer, Integer> inputSize = new HashMap(4);
        Scanner sc = new Scanner(System.in);

        for (int i=0; i<4; i++)
            inputSize.put(i, sc.nextInt());

        for (int i=0; i<4; i++) {
            ArrayList<Integer> setList = new ArrayList();
            for (int j=0; j<inputSize.get(i); j++) {
                setList.add(sc.nextInt());
            }
            inputList.add(setList);
        }

        for (int i=0; i<4; i++) {
            System.out.print("Set " + i + " has ");
            System.out.print(inputList.get(i).toString());
            System.out.println();
        }

        for (int a=0; a<inputSize.get(a); a++) {
            int aCount = (int) inputList.get(0).get(a);
            for (int b=0; b<inputSize.get(b); b++) {
                int bCount = (int) inputList.get(1).get(b);
                for (int c=0; c<inputSize.get(c); c++) {
                    int cCount = (int) inputList.get(2).get(c);
                    for (int d=0; d<inputSize.get(d); d++) {
                        int dCount = (int) inputList.get(0).get(d);
                        if (aCount + bCount + cCount + dCount == 0) {
                            System.out.printf("%d %d %d %d \n", aCount, bCount, cCount, dCount);
                            return;
                        }
                    }
                }
            }
        }
        System.out.println("No valid set");

    }
}
