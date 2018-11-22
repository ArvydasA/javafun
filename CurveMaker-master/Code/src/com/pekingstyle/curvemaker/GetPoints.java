package com.pekingstyle.curvemaker;

import java.util.HashMap;



public class GetPoints {
	
	public static HashMap<Double,Double> initPointArray(HashMap<Double, Double> point){
		
		 
		point.put(0.1, 1.25) ;
		point.put(0.25, 2.25) ;
		point.put(0.5, 3.25) ;
		point.put(0.75, 3.55) ;
		point.put(1.0 , 3.85) ;
		point.put(1.12, 4.15) ;
		point.put(1.5, 4.25) ;	
		System.out.println(point);
		
		System.out.println(point.size());
		
		return point;
	}
		
	
}
