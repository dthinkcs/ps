public class Main {
    public static void main(String[] args) {
        ComparableRectangle rect1 = new ComparableRectangle(10, 20);
        ComparableRectangle rect2 = new ComparableRectangle(30, 20);
        System.out.println(rect1.compareTo(rect2));

    }
}

class Rectangle {
    double length;
    double width;
    public Rectangle(double l, double w) {
        length = l;
        width = w;
    }
    public double getArea() {
        return length * width;
    }
}

class ComparableRectangle extends Rectangle implements Comparable<ComparableRectangle> {
    public ComparableRectangle(double l, double w) {
        super(l, w);
    }
    // method where we compare the two objects 
    public int compareTo(ComparableRectangle other) {
        if (this.getArea() < other.getArea()) {
            return -1;
        } else if (this.getArea() > other.getArea()) {
            return 1;
        } else {
            return 0;
        }
    }
}