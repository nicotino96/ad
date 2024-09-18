public class Mouse {
    private boolean isLeftHanded;

    public Mouse(boolean isLeftHanded) {
        this.isLeftHanded = isLeftHanded;
    }
    public void clickLeft(){
        if (isLeftHanded){
            System.out.println("Has hecho click secundario");
        }
        else
            System.out.println("Has hecho click principal");
    }
    public void rightButton(){
        if(!isLeftHanded)
            System.out.println("Has hecho click secundario");
        else
            System.out.println("Has hecho click principal");
    }
}
