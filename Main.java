import java.util.*;

public class Main {


	public static void main(String args[]){
		ChacoCanyon c1 = new ChacoCanyon();
		int count = 0;
		boolean ruler = true;
		System.out.println("Congratulations, you are the newest leader of ancient Chaco Canyon, elected for");
		System.out.println("a ten-year term of office. Your duties are to dispense food, direct farming,");
		System.out.println("and buy and sell land as needed to support your people. Watch out for rat");
		System.out.println("infestations and the drought! Maize is the general currency, measured in");
		System.out.println("bushels. The following will help you in your decisions:");

		System.out.println(" - Each person needs at least 20 bushels of maize per year to survive.");
		System.out.println(" - Each person can farm at most 10 acres of land.");
		System.out.println(" - It takes 2 bushels of maize to farm an acre of land.");
		System.out.println(" - The market price for land fluctuates yearly.");

		System.out.println("Rule wisely and you will be showered with appreciation at the end of your term.");
		System.out.println("Rule poorly and you will be kicked out of office!");

		while(ruler == true && count < 10){
			ruler = simulateYear(c1);
			count++;
		}
		if(count == 10 && ruler == false){
			System.out.println("You made it to your last year in office, leader! Despite what may have happened in previous years your last year in office was memorable!");
			System.out.println("In your final year in office, " + c1.getYear() + ",");
			if(c1.getStarved()==1){
				System.out.print( c1.getStarved() + " person");
			} else {
				System.out.print(c1.getStarved() + " people");
			}
			System.out.print(" starved to death, ");
			if(c1.getAbandoners()==1){
				System.out.print( c1.getAbandoners() + " person");
			} else {
				System.out.print(c1.getAbandoners() + " people");
			}
			System.out.print(" left our nation, ");
			if(c1.getImmigrants()==1){
				System.out.print( c1.getImmigrants() + " person");
			} else {
				System.out.print(c1.getImmigrants() + " people");
			}
			System.out.print(" entered our nation.  The");
			
			System.out.println(" population is now " + c1.getVillagers() + ".  The nation now owns " + c1.getLands() +" acres. This comes out to " + Math.round(c1.getLands()/c1.getVillagers()) + " acres per person.");

			if(c1.getHarvest()>0){
				System.out.print("We harvested " + c1.getHarvest());
			}else{
				System.out.print("Perhaps you should've consulted your advisors, great leader. We had no net gain yet we lost " + Math.abs(c1.getHarvest()));
			}
			System.out.print(" bushels at " + c1.getBPA() +  " bushels per acre.  Rats destroyed " + c1.getRatsAte() +  " bushels, leaving "+ c1.getBushels() + " bushels");
			System.out.println(" in storage.  Land is currently worth " + c1.getLandValue() + " bushels per acre.");
			
			if((c1.getAbandoners() + c1.getStarved()> (.3*c1.getVillagers())) || Math.round(c1.getLands()/c1.getVillagers())>5){
			System.out.println("You were an irresponsible leader but you have carried our nation to another year and another era for a more responsible leader and for that you will be remembered.");
			}
		} 
		if(count<10 && ruler == false){
			System.out.println("You were impeached by the people of Chaco Canyon! While " + c1.getAbandoners() + " people left Chaco Canyon in search of more just rulers, those who remained knew you were not fit to rule when you let " + c1.getStarved() + " people die from starvation!");
			System.out.println("You have been exiled and condemnded to wander the wastelands surrounding Chaco Canyon for an indefinite period of time. May you be better at managing your own faculties than you were at managing a nation's.");
		}
	}

	
	public static boolean simulateYear(ChacoCanyon c1){
		boolean ruler = true;
		int landsBought =0;
		int landsSold = 0;
		int bushelsFeed = 0;
		int acresSeed=0;

		//status update message

		boolean done = true;
		System.out.println("O great Chaco Leader, I beg to report to you, In the year " + c1.getYear() + ",");
		if(c1.getStarved()==1){
			System.out.print( c1.getStarved() + " person");
		} else {
			System.out.print(c1.getStarved() + " people");
		}
		System.out.print(" starved to death, ");
		if(c1.getAbandoners()==1){
			System.out.print( c1.getAbandoners() + " person");
		} else {
			System.out.print(c1.getAbandoners() + " people");
		}
		System.out.print(" left our nation, ");
		if(c1.getImmigrants()==1){
			System.out.print( c1.getImmigrants() + " person");
		} else {
			System.out.print(c1.getImmigrants() + " people");
		}
		System.out.print(" entered our nation.  The");
		System.out.println(" population is now " + c1.getVillagers() + ".  The nation now owns " + c1.getLands() +" acres.");

		if(c1.getHarvest()>0){
			System.out.print("We harvested " + c1.getHarvest());
		}else{
			System.out.print("Perhaps you should consult your advisors, great leader. We had no net gain yet we lost " + Math.abs(c1.getHarvest()));
		}
		System.out.print(" bushels at " + c1.getBPA() +  " bushels per acre.  Rats destroyed " + c1.getRatsAte() +  " bushels, leaving "+ c1.getBushels() + " bushels");
		System.out.println(" in storage.  Land is currently worth " + c1.getLandValue() + " bushels per acre.");
		Scanner in = new Scanner(System.in);

		//asking user for input

		//buying or selling land
		boolean word = false;
		do{
			System.out.printf("How many acres do you wish to buy?: ");
			//read in an int
			landsBought=0;
			try{
				landsBought = in.nextInt( );
				word = true;
				// catch bad input
			}catch (InputMismatchException e){
				System.out.println("That is not a number!");
				in.next();
			}
		}while(!word || landsBought*c1.getLandValue()>c1.getBushels());



		if(landsBought==0){
			word = false;
			do{
				System.out.printf("How many acres do you wish to sell?: ");
				//read in an int
				landsSold=0;
				try{
					landsSold = in.nextInt( );
					word = true;
					// catch bad input
				}catch (InputMismatchException e){
					System.out.println("That is not a number!");
					in.next();
				}

			}while(!word || landsSold>c1.getLands());
		}else{
			landsSold=0;
		}

		if(landsBought>0){
			c1.setLands(c1.getLands()+landsBought);
			c1.setBushels(c1.getBushels() - (c1.getLandValue() * landsBought));
		}else{
			c1.setLands(c1.getLands()-landsSold);
			c1.setBushels(c1.getBushels() + (c1.getLandValue() * landsSold));
		}	

		//ask for bushels of maize to feed people
		done = false;
		do{
			try{
				System.out.printf("How many bushels of maize do you wish to feed your people?");
				//read in an int
				bushelsFeed=0;

				try{
					bushelsFeed = in.nextInt( );
					done = true;
					if(bushelsFeed > c1.getBushels()){
						done = false;
						throw new ArithmeticException("You do not have that many bushels to give!");
					}

					// catch bad input
				}catch (InputMismatchException e){
					System.out.println("That is not a number!");
					in.next();
				}

			}catch (ArithmeticException j) {
				System.out.println(j.getMessage());
			}
		}while(!done || bushelsFeed > c1.getBushels());

		c1.setBushels(c1.getBushels() - bushelsFeed);

		//ask for acres to plant

		done = false;
		do{
			try{
				System.out.printf("How many acres do you wish to plant with seed?");
				acresSeed=0;
				try{
					acresSeed=in.nextInt( );
					done = true;
					if((acresSeed/2) > c1.getBushels()){
						done = false;
						throw new ArithmeticException("You do not have enough bushels to plant seed on that many acres!");
					}

					if((c1.getVillagers()<acresSeed/10)){
						done = false;
						throw new ArithmeticException("You do not have enough villagers to harvest your desired amount of acreage!");
					}

					if((acresSeed>c1.getLands())){
						done=false;
						throw new ArithmeticException("You do not have enough land!");
					}
					// catch bad input
				}catch (InputMismatchException e){
					done = false;
					System.out.println("That is not a number!");
					in.next();
				}

			} catch(ArithmeticException g){
				done = false;
				System.out.print(g.getMessage());
				
			}
		} while (!done || ((acresSeed/2) > c1.getBushels()) || (c1.getVillagers()<acresSeed/10));

		c1.setBushels(c1.getBushels() - (2*acresSeed));


		//what happens if there is a drought

		c1.setYear(c1.getYear()+1);
		boolean starvation;
		boolean drought;
		Random generator = new Random();
		int weather = generator.nextInt(22);
		if(weather == 0 || weather == 1 || weather == 2){
			drought = true;
		} else {
			drought = false;
		}

		if(drought == true){
			if((c1.getVillagers() - bushelsFeed/20)<0){
				c1.setStarved(Math.round((int)((c1.getVillagers()-c1.getAbandoners())*.3)));
			}else{
				c1.setStarved(Math.round((int)((c1.getVillagers()-c1.getAbandoners())*.3)) + (c1.getVillagers() - bushelsFeed/20));
			}
			c1.setLeft(Math.round((int)(c1.getVillagers()*.2)));
			c1.setVillagers(c1.getVillagers() - (c1.getStarved() + c1.getAbandoners()));
			System.out.println("The gods have not been kind to us this year, leader! Drought has ravaged our nation and left many anxious and desperate. This does not bode well for you, great leader.");

		}


		//what happens if people starve

		if((bushelsFeed/20)<c1.getVillagers()){
			starvation = true;
		}
		else{
			starvation = false;
		}
		if(starvation == true){
			c1.setStarved((c1.getVillagers() - bushelsFeed/20));
			c1.setVillagers(c1.getVillagers() - c1.getStarved());
			c1.setEntered(0);
		}else{
			Random random = new Random();
			double P = random.nextDouble();
			int x = 20 * c1.getLands() + c1.getBushels();
			int y = 100 * c1.getVillagers();
			int z = ((x/y)+1);
			int a = (int)(z * P);
			if(drought==true){
				c1.setStarved(c1.getStarved());
				c1.setEntered(0);
			}else{
				c1.setEntered(a);
				c1.setVillagers(c1.getVillagers() + c1.getImmigrants());
				c1.setStarved(0);

			}
		}

		//calculate harvest and bushels Stored
		c1.setbPa(1 + (int)(Math.random() * ((8-1) + 1)));
		int cost = 2*acresSeed;
		c1.setHarvest((acresSeed * c1.getBPA())-(cost));
		if(c1.getHarvest()>0){
			c1.setBushels(c1.getBushels() + c1.getHarvest());
		} else {
			c1.setBushels(c1.getBushels());
		}



		//what happens if there is rats

		boolean rats;
		Random random = new Random();
		int Ratties = random.nextInt(2);
		if(Ratties == 0){
			rats = true;
		} else {
			rats = false;
		}

		if(rats == true){
			Random x = new Random();
			double ratFrac = .04 + (.4-.04) * x.nextDouble();

			int ratsAte = (int)(c1.getBushels() * ratFrac);
			c1.setRatsAte(ratsAte);
			c1.setBushels(c1.getBushels() - ratsAte);
		}

		//land Valuation
		c1.setLandValue(17 + (int)(Math.random() * (26- 17) + 1));

		if(c1.getVillagers()*.45 < (c1.getStarved()+c1.getAbandoners())){
			ruler = false;
		}
		return ruler;
	}
}


