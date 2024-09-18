public class TravelStops {
    private String[] stops;
    public TravelStops(){
        stops = new String[]{"Tokyo",
        "Frankfurt",
        "Kuala Lumpur"};
    }
    public void printFirstStop() {
        System.out.println(this.stops[0]);
    }

    public void printSecondStop() {
        System.out.println(this.stops[1]);
    }

    public void printThirdStop() {
        System.out.println(this.stops[2]);
    }
    public void printStop(int position) {
        System.out.println(this.stops[position]);
    }
    public void printEveryStop(){
        for(int i=0;i< stops.length;i++){
            System.out.println(stops[i]);
        }
    }

}

