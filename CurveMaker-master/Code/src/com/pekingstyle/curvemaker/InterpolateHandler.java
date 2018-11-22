package com.pekingstyle.curvemaker;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

public class InterpolateHandler {

	/*
	 * 判断使用哪种插值方法： 1. 线性插值 2. 拉格朗日插值 3. 赫拉米特插值 使用对应的系数，调用不同的插值方法
	 */
	public static HashMap<Double, Double> point = new HashMap<Double,Double>();

	public static double[] x;
	public static String[] y;

	public static void main(String args[]) {

		doLiner(GetPoints.initPointArray(point));

	}

	private static void doLiner(HashMap<Double, Double> point) {
		Iterator i = point.entrySet().iterator();
		
		while(i.hasNext()){
		Entry e =(java.util.Map.Entry) i.next();
		System.out.println(e.getKey());
		}
	}


		
	
}
