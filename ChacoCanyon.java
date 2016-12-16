import java.util.Scanner;
class ChacoCanyon {
	

private int villagers;
private int bushelsStorage;
private int lands;	
private int landValue;
private int year;

private int starved;
private int left;
private int entered;
private int ratsAte;
private int harvest;
private int bPa;

public ChacoCanyon() {
	//a private variable
	

	this.villagers = 100;
	this.bushelsStorage=3000;
	this.lands=1000;
	this.landValue=20;
	this.year=1000;
}


//set number of villagers
public void setVillagers(int villagers){
	this.villagers = villagers;
}
//set number of people starved
public void setStarved(int starved){
	this.starved = starved;
}
//set number of people who left
public void setLeft(int left){
	this.left = left;
}
//set number of people who entered
public void setEntered(int entered){
	this.entered = entered;
}
//set number of bushels harvested
public void setHarvest(int harvest){
	this.harvest = harvest;
}
//set number of bushels harvested
public void setbPa(int bPa){
	this.bPa = bPa;
}
//set number of bushels rats ate
public void setRatsAte(int ratsAte){
	this.ratsAte = ratsAte;
}
//set number of bushels in storage
public void setBushels(int bushelsStorage){
	this.bushelsStorage = bushelsStorage;
}
//set value of land
public void setLandValue(int landValue){
	this.landValue=landValue;
}

public void setLands(int lands){
	this.lands = lands;
}

public void setYear(int year){
	this.year=year;
}


//return number of villagers
public int getVillagers(){
	return villagers;
}
//return number of bushels
public int getBushels(){
	return bushelsStorage;
}
//return number of acreage
public int getLands(){
	return lands;
}
//return value of land
public int getLandValue(){
	return landValue;
}
public int getYear(){
	return year;
}
//return number of starved
public int getStarved(){
	return starved;
}

//return number of people who leave
public int getAbandoners(){
	return left;
}
//return number of people who enter
public int getImmigrants(){
	return entered;
}
//return number of bushels rats ate
public int getRatsAte(){
	return ratsAte;
}
//return the harvest
public int getHarvest(){
	return harvest;
}

//return the bushels per acre
public int getBPA(){
	return bPa;
}



}