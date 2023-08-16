diff --git a/scp_jp_conv/map/0/EV00120.txt b/scp_conv/map/0/EV00120.txt
index a5df571..64a3fa7 100644
--- a/scp_jp_conv/map/0/EV00120.txt
+++ b/scp_conv/map/0/EV00120.txt
@@ -216,8 +216,9 @@ INIT
 		{
 		//	set_chr( MEI,49,		-1,-1,	763,-290,0,		52,90,20,"<TK_MEI>")		//宿酒場　ペンギンの前　メイ
 			set_chr( MEI,49,	-1,-1,  800,-850,1,  	50,30, 20,"<TK_MEI>")			//宿酒場　カウンター　メイ
-			set_chr( PENGUIN,81,	-1,-1,	734,-542,0,		2,190,20,"<TK_PENGUIN>")	//呼び込みペンギン
-			
+//			set_chr( PENGUIN,81,	-1,-1,	734,-542,0,		2,190,20,"<TK_PENGUIN>")	//呼び込みペンギン
+			set_chr( PENGUIN,81,	-1,-1,	840,-542,0,		2,190,20,"<TK_PENGUIN>")	//呼び込みペンギン	//パッチ 2008/09/22
+
 			//モーション
 			MOT_SET(MEI,150,-1,476,476,-1,15)		//メイ
 			MOT(MEI,150,0)
@@ -237,7 +238,8 @@ INIT
 		//モーション
 		MOT_SET(SHESTOR,150,-1,260,319,-1,0)	//シェスター　腕組
 		MOT(SHESTOR,150,0)
-		MOT_SET(CEPHEILA,150,-1,560,560,-1,0)	//セフィーラ　ベッドに腰掛
+	//	MOT_SET(CEPHEILA,150,-1,560,560,-1,0)	//セフィーラ　ベッドに腰掛
+		MOT_SET(CEPHEILA,150,-1,554,554,-1,0)	//セフィーラ　ベッドに腰掛0922モーション変更
 		MOT(CEPHEILA,150,0)
 		MOT_SET(TEO,150,-1,577,577,-1,0)		//テオ　座る
 		MOT(TEO,150,0)
@@ -613,7 +615,7 @@ ROOT_MOVE_MEI
 MOVE_MEI
 {
 //	一つ目のテーブルへ
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1,	257,-1152,0, 0)
 	wait_move( MEI )
 //	rot(MEI,60,72)
@@ -622,21 +624,21 @@ MOVE_MEI
 	
 //	rot(MEI,60,351)
 
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, 327,-1012,1,	0)
 	wait_move( MEI )
 	
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, 271,-948,0,	0)
 	wait_move( MEI )
 //	rot(MEI,60,90)
 	
 //	2つ目のテーブルへ
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -398,-1015,0,	0)
 	wait_move( MEI )
 //	rot(MEI,60,353)
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -492,-941,1,	0)
 	wait_move( MEI )
 
@@ -644,11 +646,11 @@ MOVE_MEI
 
 //	3つ目のテーブルへ
 //	rot(MEI,60,146)
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -598,-1180,1,	0)	
 	wait_move( MEI )
 //	rot(MEI,60,97)
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -756,-1175,0,	0)
 	wait_move( MEI )
 
@@ -656,14 +658,14 @@ MOVE_MEI
 
 //	初期位置へ
 //	rot(MEI,60,247)							
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -405,-1209,1,	0)
 	wait_move( MEI )
 //	rot(MEI,60,239)							
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, -181,-1431,1,	0)
 	wait_move( MEI )
-	if(!F202)
+//	if(!F203)
 	move( MEI, 20,	WALK1, 298,-1505,1,		0)
 	wait_move( MEI )
 //	rot(MEI,60,351)
diff --git a/scp_jp_conv/map/0/EV00145.txt b/scp_conv/map/0/EV00145.txt
index e88a230..399301a 100644
--- a/scp_jp_conv/map/0/EV00145.txt
+++ b/scp_conv/map/0/EV00145.txt
@@ -102,46 +102,46 @@ INIT
 
 
 	//ティラノを囲むロープ
-	set_chr(300, 716, 	2,4,	0,40,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(301, 716, 	2,4,	-340,-330,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(302, 716, 	2,4,	340,-330,0,		0,	270,0,";")	//博物館ロープ		obx0500
-	set_chr(303, 716, 	2,4,	-250,-70,0,		0,	45,	0,";")	//博物館ロープ		obx0500
-	set_chr(304, 716, 	2,4,	250,-70,0,		0,	315,0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,4,	0,40,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,4,	-340,-330,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,4,	340,-330,0,		0,	270,0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,4,	-250,-70,0,		0,	45,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,4,	250,-70,0,		0,	315,0,";")	//博物館ロープ		obx0500
 
 	//ステゴを囲むロープ
-	set_chr(305, 716, 	3,2,	0,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(306, 716, 	3,2,	350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(307, 716, 	3,2,	-350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,2,	0,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,2,	350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,2,	-350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
 
 	//トリケラを囲むロープ
-	set_chr(308, 716, 	1,2,	0,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(309, 716, 	1,2,	350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(310, 716, 	1,2,	-350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,2,	0,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,2,	350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,2,	-350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
   
   	//首長竜を囲むロープ
-	set_chr(311, 716, 	2,2,	0,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(312, 716, 	2,2,	350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
-	set_chr(313, 716, 	2,2,	-350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,2,	0,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,2,	350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	2,2,	-350,110,0,			0,	0,	0,";")	//博物館ロープ		obx0500
                               
 	//シーラカンス～アノマロカリスを囲むロープ
-	set_chr(370, 716, 	3,3,	-30,-30,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(371, 716, 	3,3,	-30,320,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(372, 716, 	3,3,	-30,640,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(373, 716, 	3,3,	-30,960,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(374, 716, 	3,3,	-30,1280,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(375, 716, 	3,3,	-30,1600,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(376, 716, 	3,3,	-30,1920,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(377, 716, 	3,3,	100,-200,0,	0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,-30,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,320,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,640,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,960,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,1280,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,1600,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	-30,1920,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	3,3,	100,-200,0,	0,	0,	0,";")	//博物館ロープ		obx0500
 	
 	//シードラゴン～ジュゴンを囲むロープ
-	set_chr(378, 716, 	1,3,	30,-30,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(379, 716, 	1,3,	30,320,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(380, 716, 	1,3,	30,640,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(381, 716, 	1,3,	30,960,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(382, 716, 	1,3,	30,1280,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(383, 716, 	1,3,	30,1600,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(384, 716, 	1,3,	30,1920,0,	0,	90,	0,";")	//博物館ロープ		obx0500
-	set_chr(385, 716, 	1,3,	-100,-200,0,	0,	0,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,-30,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,320,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,640,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,960,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,1280,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,1600,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	30,1920,0,	0,	90,	0,";")	//博物館ロープ		obx0500
+	set_chr(36, 716, 	1,3,	-100,-200,0,	0,	0,	0,";")	//博物館ロープ		obx0500
 	
 	
 	                            
@@ -160,13 +160,13 @@ INIT
 //ノード制御
 	//---------------------------首長---------------------------------
 	workL(5,SET,0)//寄贈状況
-	if(F2325)
+	if(F2425)
 		workL(5,ADD,1)
-	if(F2326)
+	if(F2426)
 		workL(5,ADD,1)
-	if(F2327)
+	if(F2427)
 		workL(5,ADD,1)
-	if(F2328)
+	if(F2428)
 		workL(5,ADD,1)
 
 	if(WK005<4)
@@ -189,13 +189,13 @@ INIT
 	}
 	//---------------------------ティラノ---------------------------------
 	workL(5,SET,0)//寄贈状況
-	if(F2329)
+	if(F2429)
 		workL(5,ADD,1)
-	if(F2330)
+	if(F2430)
 		workL(5,ADD,1)
-	if(F2331)
+	if(F2431)
 		workL(5,ADD,1)
-	if(F2332)
+	if(F2432)
 		workL(5,ADD,1)
 
 	if(WK005<4)
@@ -218,13 +218,13 @@ INIT
 	}
 	//---------------------------ステゴ---------------------------------
 	workL(5,SET,0)//寄贈状況
-	if(F2333)
+	if(F2433)
 		workL(5,ADD,1)
-	if(F2334)
+	if(F2434)
 		workL(5,ADD,1)
-	if(F2335)
+	if(F2435)
 		workL(5,ADD,1)
-	if(F2336)
+	if(F2436)
 		workL(5,ADD,1)
 
 	if(WK005<4)
@@ -247,13 +247,13 @@ INIT
 	}
 	//---------------------------トリケラ---------------------------------
 	workL(5,SET,0)//寄贈状況
-	if(F2337)
+	if(F2437)
 		workL(5,ADD,1)
-	if(F2338)
+	if(F2438)
 		workL(5,ADD,1)
-	if(F2339)
+	if(F2439)
 		workL(5,ADD,1)
-	if(F2340)
+	if(F2440)
 		workL(5,ADD,1)
 
 	if(WK005<4)
diff --git a/scp_jp_conv/map/0/EV00146.txt b/scp_conv/map/0/EV00146.txt
index a3f825a..2be209d 100644
--- a/scp_jp_conv/map/0/EV00146.txt
+++ b/scp_conv/map/0/EV00146.txt
@@ -313,7 +313,7 @@ INIT
 		F_set(NAZO)
 		
 		//ジェット見上げカメラ出現
-		set_chr( 291,990,	3,2,     0, -200,  0,    0,   0,8,"(L7?99 <CAM_NAZO> WT?30 L7!99 <CAM_RESET>);")
+		set_chr( 81,990,	3,2,     0, -200,  0,    0,   0,8,"(L7?99 <CAM_NAZO> WT?30 L7!99 <CAM_RESET>);")
 		set_chr( 170,991,	3,2,     0, -80,  0,    0,0506,0,";")//アタリ
 		set_chr( 170,991,	3,2,     0,    0,  0,    0,0603,0,";")//アタリ左右
 		set_chr( 170,991,	3,2,     0,   80,  0,    0,0303,0,";")//アタリ手前
@@ -322,13 +322,13 @@ INIT
 
 	//---------------------------ロボ①---------------------------------
 	workL(6,SET,0)//寄贈状況
-	if(F2341)
+	if(F2441)
 		workL(6,ADD,1)
-	if(F2342)
+	if(F2442)
 		workL(6,ADD,1)
-	if(F2343)
+	if(F2443)
 		workL(6,ADD,1)
-	if(F2344)
+	if(F2444)
 		workL(6,ADD,1)
 
 	if(WK006<4)
@@ -350,7 +350,7 @@ INIT
 
 	if(WK006==4)
 	{	//ロボ見上げカメラ出現
-		set_chr( 292,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
+		set_chr( 82,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
 
 	}
 //	if(WK006==4)
@@ -364,13 +364,13 @@ INIT
 //	}
 	//---------------------------ロボ②---------------------------------
 	workL(7,SET,0)//寄贈状況
-	if(F2345)
+	if(F2445)
 		workL(7,ADD,1)
-	if(F2346)
+	if(F2446)
 		workL(7,ADD,1)
-	if(F2347)
+	if(F2447)
 		workL(7,ADD,1)
-	if(F2348)
+	if(F2448)
 		workL(7,ADD,1)
 
 	if(WK007<4)
@@ -391,7 +391,7 @@ INIT
 	}
 	if(WK007==4)
 	{	//ロボ見上げカメラ出現
-		set_chr( 293,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
+		set_chr( 83,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
 	}
 //	else
 //	{
@@ -703,7 +703,7 @@ LP_ROBO1
 	if(WK006==4)
 	{
 //		MES(ROBO1_TXT,"C4W9キャプテン２１号【Ｃａｐｔａｉｎ＿21】\n――ヘイ兄貴！\nオレはどこまでも付いて行くぜ！\n（※ノリっぽい説明文募集中。\n＿おもちゃの謳い文句など）",0)
-		MES(ROBO1_TXT,"C4W9キャプテン２１号【Ｃａｐｔａｉｎ＿21】\nやっと完成、古き良きブリキのおもちゃ。\n稼動部は少なめだがそこに味がある。",0)
+		MES(ROBO1_TXT,"C4W9キャプテン２１号【Ｃａｐｔａｉｎ＿21】\nやっと完成、古き良きブリキのおもちゃ。\n可動部は少なめだがそこに味がある。",0)
 		MES(ROBO1_TXT,"C4W9──やぁ、オイラはキャプテン２１号！\n電池の続く限りどこまでも步くよ！\n小さいお子様の手の届かないところに保管してね！",0)
 		MES_close(ROBO1_TXT)
 		wait_MES(ROBO1_TXT)
@@ -717,7 +717,7 @@ LP_ROBO1
 	//	if(!FT_FF_TalkROBO1)
 		if(!FT_FF_TalkROBO1 && !F6_05_EndSixth)		//エピローグでは発生しない
 		{
-			delete(292)
+			delete(82)
 			wait(2)
 
 			cross_fade(20)
@@ -908,7 +908,7 @@ LP_ROBO1
 			F_set(FT_FF_TalkROBO1)
 
 			look_del(RAGNA)
-			set_chr( 292,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
+			set_chr( 82,990,	2,1,     -300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO1> WT?30 L2!99 <CAM_RESET>);")	
 
 			fade_in(0,30,BLACK)
 			wait_fade()
@@ -1052,7 +1052,7 @@ LP_ROBO2
 	//	if(!FT_FF_TalkROBO2)
 		if(!FT_FF_TalkROBO2 && !F6_05_EndSixth)		//エピローグでは発生しない
 		{
-			delete(293)
+			delete(83)
 			wait(2)
 
 			cross_fade(20)
@@ -1190,7 +1190,7 @@ LP_ROBO2
 
 		//	name("フレイムバイザー")
 			MES(ROBO2,"W9L711勇者といえば正義の拳。\nL711正義の拳といえばアッパーボムだ。",0)
-			MES(ROBO2,"W9L711その拳を持って\nL711己の正義を貫いてみせるがいい……！",0)
+			MES(ROBO2,"W9L711その拳をもって\nL711己の正義を貫いてみせるがいい……！",0)
 			MES_close(ROBO2)
 
 
@@ -1202,7 +1202,7 @@ LP_ROBO2
 			F_set(FT_FF_TalkROBO2)
 
 			look_del(RAGNA)
-			set_chr( 293,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
+			set_chr( 83,990,	2,1,     300, -50,  0,    0,0501,8,"(L1?99 <CAM_ROBO2> WT?30 L2!99 <CAM_RESET>);")	
 
 			fade_in(0,30,BLACK)
 			wait_fade()
diff --git a/scp_jp_conv/map/0/EV00301.txt b/scp_conv/map/0/EV00301.txt
index 7aff059..a0cebb8 100644
--- a/scp_jp_conv/map/0/EV00301.txt
+++ b/scp_conv/map/0/EV00301.txt
@@ -816,7 +816,9 @@ EV_3_01_MonsterVillage
 		get_item(003,-1,1)		// 消す(グライドギア)
 	if(IT004>0)					// 持っていたら
 		get_item(004,-1,1)		// 消す(ブレードギア)
-
+	if(IT005>0)					// 持っていたら
+		get_item(005,-1,1)		// 消す(マッスルギア)
+		
 	wait(10)
 	SE(043,PLAYER1)
 //	MES(RAGNA,"C3S2フックギアを装備しました。\n村人たちを背後からフックギアで捕まえて\nアルウェンの元へ運んでください。",2)
@@ -896,7 +898,9 @@ EV_3_01_MonsterOnly
 		get_item(003,-1,1)		// 消す(グライドギア)
 	if(IT004>0)					// 持っていたら
 		get_item(004,-1,1)		// 消す(ブレードギア)
-
+	if(IT005>0)					// 持っていたら
+		get_item(005,-1,1)		// 消す(マッスルギア)
+		
 	set_chr(ALWEN,	1011,-1,-1, 1,1,1, 2,0,8, "<EV_JYOUKA>")
 	set_chr(LUE,	 1015,-1,-1, 1,1,1, 2,0,0, "")
 	set_chr(ZONBI_A,	384,-1,-1, 1,1,1, 2,0,9, "RF200 Z1?06 L4?12 SF200")
@@ -1069,7 +1073,9 @@ EV_3_02_DEBUG
 		get_item(003,-1,1)		// 消す(グライドギア)
 	if(IT004>0)					// 持っていたら
 		get_item(004,-1,1)		// 消す(ブレードギア)
-
+	if(IT005>0)					// 持っていたら
+		get_item(005,-1,1)		// 消す(マッスルギア)
+		
 	set_chr(ALWEN,	1011,-1,-1, 1,1,1, 2,0,0, "")
 	set_chr(LUE,	 1015,-1,-1, 1,1,1, 2,0,0, "")
 	set_chr(ZONBI_A,	384,-1,-1, 1,1,1, 2,0,0, "")
@@ -1220,7 +1226,9 @@ EV_3_02_GoMoonCastle
 		get_item(003,1,1)		// １個入手(グライドギア)
 	if(IT004==0)
 		get_item(004,1,1)		// １個入手(ブレードギア)
-
+	if(IT005==0)
+		get_item(005,1,1)		// １個入手(マッスルギア)
+		
 	set_chr(EVENT_RAGNA,	  1010,-1,-1, 180,3560,-22, 2,195,0, "")
 	chr_pos(ALWEN,	530,3920,-22,10,2)
 	chr_pos(LUE, 	690,3850,-22,70,2)
diff --git a/scp_jp_conv/map/0/EV00400.txt b/scp_conv/map/0/EV00400.txt
index 47ebe8d..44e370e 100644
--- a/scp_jp_conv/map/0/EV00400.txt
+++ b/scp_conv/map/0/EV00400.txt
@@ -299,7 +299,7 @@ INIT
 		set_chr( NINJYA_F,490,-1,-1, -157,-3460,1,	2,34, 20,"<TK_NINJYA_F>")		//星降りの里．カイの傍で倒れている　忍者Ｆ
 
 		
-		set_chr( 97,990,	-1,-1,  -359,-13227,1476,	   0,  0505, 6,"<EV_STOP_KARASU>")	//ストッパー：脱衣所
+		set_chr( 81,990,	-1,-1,  -359,-13227,1476,	   0,  0505, 6,"<EV_STOP_KARASU>")	//ストッパー：脱衣所
 
 		if(!FS_10_TalkKarasu)
 		{
@@ -355,7 +355,7 @@ INIT
 		F_set_chr(NINJYA_H_2,CF_NO_MOVE)
 		F_set_chr(NINJYA_H_3,CF_NO_MOVE)
 		F_set_chr(NINJYA_H_4,CF_NO_MOVE)
-		F_set_chr(KARASU,CF_NO_MOVE)
+	//	F_set_chr(KARASU,CF_NO_MOVE)	//0924コメント化
 	}
 	else
 	//──────────────────────────────
@@ -417,7 +417,8 @@ INIT
 		//ルリ初回後　分身4人目出現
 		if(FS_08_TalkLuri)
 		{
-			set_chr( LURI_4,77,		-1,-1,	7495,-9945,1399,	2,0, 20,"<TK_LURI_4>")					//星降りの里．お稲荷さん近く　ルリ分身4
+//			set_chr( LURI_4,77,		-1,-1,	7495,-9945,1399,	2,0, 20,"<TK_LURI_4>")					//星降りの里．お稲荷さん近く　ルリ分身4
+			set_chr( LURI_4,77,		-1,-1,	6530,-10404,1660,	2,0, 20,"<TK_LURI_4>")					//星降りの里．岩の上　ルリ分身4　パッチ 2008/09/22
 			MOT_SET(LURI_4,150,-1,552,552,-1,-1)
 			MOT(LURI_4,150,0)
 			EV("ROLING_LURI")
@@ -442,9 +443,9 @@ INIT
 		//里のキャラに一通り話すとイベントエントリーが出現
 		if(F4_12_OkRoten && !F4_15_EndSatolook)
 		{
-			set_chr( 300,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//階段下
-			set_chr( 301,990,	-1,-1,   658,-10864,1400,	   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//階段上
-			set_chr( 302,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//橋の上
+			set_chr( 82,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//階段下
+			set_chr( 83,990,	-1,-1,   658,-10864,1400,	   2,083404, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//階段上
+			set_chr( 84,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//橋の上
 		}
 		
 		//里のキャラに一通り話すとサラサは消える
@@ -713,9 +714,9 @@ EV_F4_12_OkRoten
 	//ヒコメのみ別マップなので仕込んでいません
 	if(FS_08_TalkHikome && FS_08_TalkKarasu && FS_08_TalkDaigoro && FS_08_TalkYasaku && FS_08_TalkKai && FS_08_TalkAkane && FS_08_TalkLuri && FS_08_TalkGen)
 	{
-		set_chr( 300,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//階段下
-		set_chr( 301,990,	-1,-1,   658,-10864,1400,	   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//階段上
-		set_chr( 302,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//橋の上
+		set_chr( 82,990,	-1,-1,   1134,-8124,6,		   2,080804, 	6,"<EV_4_15_EndSatolook_KaidanShita>;")	//階段下
+		set_chr( 83,990,	-1,-1,   658,-10864,1400,	   2,083404, 	6,"<EV_4_15_EndSatolook_KaidanUe>;")	//階段上
+		set_chr( 84,990,	-1,-1,   301,-1782,56,		   2,080404, 	6,"<EV_4_15_EndSatolook_Hashi>;")		//橋の上
 
 		F_set(F4_12_OkRoten)
 	
@@ -927,9 +928,9 @@ EV_4_15_EndSatolook
 		F_set(F4_15_EndSatolook)
 		
 		//エントリを3地点から消す
-		delete(300)
-		delete(301)
-		delete(302)
+		delete(82)
+		delete(83)
+		delete(84)
 
 		EV_end()
 		
diff --git a/scp_jp_conv/map/0/EV00401.txt b/scp_conv/map/0/EV00401.txt
index f685134..7ad6ea8 100644
--- a/scp_jp_conv/map/0/EV00401.txt
+++ b/scp_conv/map/0/EV00401.txt
@@ -354,7 +354,7 @@ INIT
 		{
 			//▼魔物の群れに囲まれる～アルウェン登場
 			//								                 z x y
-			set_chr( 80,990,	-1,-1,   1075,-8300,-100,  0, 140802,6,"<EV_4_12_JoinAlwen>;")
+			set_chr( 80,990,	-1,-1,   1075,-8300,-100,  0, 201202,6,"<EV_4_12_JoinAlwen>;")		//パッチ 2008/09/22 範囲を広げる
 		}
 	}
 }
@@ -824,7 +824,8 @@ EV_4_10_AreYouSubaru3
 	F_set(F4_06_StopAttack)
 	
 	//★ラグナ【７年前】
-	F_set_note(RAGNA,2)
+	F_set_note(PLAYER1,2)				//パッチ修正 20081010
+
 	//★スバル【実は女の子】
 	F_set_note(-20,2)
 
diff --git a/scp_jp_conv/map/0/EV00431.txt b/scp_conv/map/0/EV00431.txt
index d261e99..6fb2cb1 100644
--- a/scp_jp_conv/map/0/EV00431.txt
+++ b/scp_conv/map/0/EV00431.txt
@@ -93,11 +93,13 @@ INIT
 
 		if( GW_ENTRY_EVENT==0 )
 		{
-			set_chr(EFFDUMMY1,749,	-1,-1,  -927,97,-49,55,0, 0,"")		//火の粉：
+			set_chr(EFFDUMMY1,749,	-1,-1,    680,0,0,55,0, 0,"")		//火の粉：	//パッチ修正 2008/09/22
 			F_set_chr(EFFDUMMY1,CF_NO_CSP)
+			F_set_chr(EFFDUMMY1,CF_NO_HEIGHT)
+			F_set_chr(EFFDUMMY1,CF_NO_ZIMEN)
 			map_color(80,60,60,0);//R,G,B, time 100%
 		}
-		
+
 		//モーション
 		MOT_SET(NINJYA_A, 150, -1, 523,523,-1,-1)	//倒れ
 		MOT_SET(NINJYA_C, 150, -1, 523,523,-1,-1)	//倒れ
@@ -690,8 +692,10 @@ EV_4_11_Save
 	//--- デフォルト表情 --------------------------------------------------
 	KAO(EVENT_RAGNA, "1","3","1")
 
-	set_chr(EFFDUMMY1,749,	-1,-1,  -927,97,-49,55,0, 0,"")		//火の粉：
-	F_set_chr(EFFDUMMY1,CF_NO_CSP)	
+	set_chr(EFFDUMMY1,749,	-1,-1,    680,0,0,55,0, 0,"")		//火の粉：	//パッチ修正 2008/09/22
+	F_set_chr(EFFDUMMY1,CF_NO_CSP)
+	F_set_chr(EFFDUMMY1,CF_NO_HEIGHT)
+	F_set_chr(EFFDUMMY1,CF_NO_ZIMEN)
 	map_color(80,60,60,0);//R,G,B, time 100%
 
 	look(EVENT_RAGNA, "Bone_Head", 0,2,2,2, 0,0,-20)	
diff --git a/scp_jp_conv/map/0/EV00440.txt b/scp_conv/map/0/EV00440.txt
index ea40e01..235f2e2 100644
--- a/scp_jp_conv/map/0/EV00440.txt
+++ b/scp_conv/map/0/EV00440.txt
@@ -478,6 +478,8 @@ EV_4_09_WithSubaru
 	delete(SUBARU)
 	delete(EVENT_RAGNA)
 
+	F_set(F4_17_InTheEvening)		////★夕方になった パッチ　2008/09/22 夕方フラグ立てる
+
 //露天風呂へ
 	workG(GW_ENTRY_EVENT,SET,1)
 	new_map(10451)
diff --git a/scp_jp_conv/map/0/EV00480.txt b/scp_conv/map/0/EV00480.txt
index f03385a..2f4ce14 100644
--- a/scp_jp_conv/map/0/EV00480.txt
+++ b/scp_conv/map/0/EV00480.txt
@@ -169,7 +169,7 @@ LP_MON
 		if(GW_MAN==1)
 		{
 		//　　※ラグナ先頭
-			MES(RAGNA,"こっちは入れないみたいだ。\nま、事を荒立てなくねえしな。",0)
+			MES(RAGNA,"こっちは入れないみたいだ。\nま、事を荒立てたくねえしな。",0)
 			MES_close(RAGNA)
 		}
 		else
diff --git a/scp_jp_conv/map/0/EV00490.txt b/scp_conv/map/0/EV00490.txt
index 9cc452a..ac53a63 100644
--- a/scp_jp_conv/map/0/EV00490.txt
+++ b/scp_conv/map/0/EV00490.txt
@@ -97,6 +97,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,76)	//攻略中ルート
 		workL(WK_ROUTETIME_STOP,SET,1)	// スコア計測停止
 
+		if(GW_SKI_COUNT1<255)
+		{
+			workG(GW_SKI_COUNT1,ADD,1)	//プレイ回数
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////ＨＰ0でも消えない　キャラ0は死亡時に"EV_DEAD"を再生
 		//ワープ封じ
 		workG(GW_WARP_FLAG,SET,0)//ワープ封じる。
@@ -249,39 +254,155 @@ EV_GOAL
 //	move(PLAYER1,0,RUN2,138,63079,-1002,0)//	typ[0=座標指定 1=キャラXの位置+Z 2=自分相対位置 3=自分位置＆xyzが-1以外で直位置　5=フリムブ 99=ムーブ解除]   Len=到達範囲距離 typeが20以上で自動方向変換 typeが30以上で自動モーション切り替えなし
 	CAM_Type(1)
 
-	if(GW_NOW_BREAK==28 && GW_NOW_DAM==0 && SP003<3600)
-	{
-		//達成できたらブロンズ
-		workG(GW_ENTRY_EVENT,SET,1)	//ブロンズ
-	}
-	else
-	if(SP003>3600)		//60秒=60*60sec
-	{
-		//時間オーバー
-		workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
-	}
-	else
-	if(GW_NOW_DAM!=0)
+	if(GW_SKI_DOWN==3)		// 難易度ダウン３
 	{
-		//ダメージ
-		workG(GW_ENTRY_EVENT,SET,9)	//9=スキー失敗(ダメージ)
+		if(GW_NOW_BREAK>=12 && GW_NOW_DAM<=5 && SP003<4800)
+		{
+			//達成できたらブロンズ
+			workG(GW_ENTRY_EVENT,SET,1)		//ブロンズ
+		}
+		else
+		if(SP003>4800)						//80秒=80*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>5)					//ダメージ5 回
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<9)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
+	if(GW_SKI_DOWN==2)		// 難易度ダウン２
 	{
-		//壊し足りない　ゼロ
-		workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		if(GW_NOW_BREAK>=20 && GW_NOW_DAM<=3 && SP003<4200)
+		{
+			//達成できたらブロンズ
+			workG(GW_ENTRY_EVENT,SET,1)		//ブロンズ
+		}
+		else
+		if(SP003>4200)						//70秒=70*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>3)					//ダメージ3回
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<17)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<25)
+	if(GW_SKI_DOWN==1)		// 難易度ダウン１
 	{
-		//壊し足りない　足りない
-		workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		if(GW_NOW_BREAK>=24 && GW_NOW_DAM<=1 && SP003<3900)
+		{
+			//達成できたらブロンズ
+			workG(GW_ENTRY_EVENT,SET,1)		//ブロンズ
+		}
+		else
+		if(SP003>3900)						//65秒=65*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>1)					//ダメージ1回
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<21)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
 	{
-		//壊し足りない　おしい
-		workG(GW_ENTRY_EVENT,SET,8)	//8=スキー失敗(ツボ、おしい)
+		if(GW_NOW_BREAK==28 && GW_NOW_DAM==0 && SP003<3600)
+		{
+			//達成できたらブロンズ
+			workG(GW_ENTRY_EVENT,SET,1)		//ブロンズ
+		}
+		else
+		if(SP003>3600)						//60秒=60*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM!=0)					//ダメージ０回
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<25)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 
 	//暗転
diff --git a/scp_jp_conv/map/0/EV00491.txt b/scp_conv/map/0/EV00491.txt
index b5898ca..8e1238c 100644
--- a/scp_jp_conv/map/0/EV00491.txt
+++ b/scp_conv/map/0/EV00491.txt
@@ -115,6 +115,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,77)	//攻略中ルート
 		workL(WK_ROUTETIME_STOP,SET,1)	// スコア計測停止
 
+		if(GW_SKI_COUNT2<255)
+		{
+			workG(GW_SKI_COUNT2,ADD,1)	//プレイ回数
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////ＨＰ0でも消えない　キャラ0は死亡時に"EV_DEAD"を再生
 		//ワープ封じ
 		workG(GW_WARP_FLAG,SET,0)//ワープ封じる。
@@ -261,39 +266,155 @@ EV_GOAL
 	SE(24,0)
 	CAM_Type(1)
 
-	if(GW_NOW_BREAK==36 && GW_NOW_DAM==0 && SP003<2700)		//45秒=45*60sec
-	{
-		//達成できたらシルバー
-		workG(GW_ENTRY_EVENT,SET,2)	//シルバー
-	}
-	else
-	if(SP003>2700)		//45秒=45*60sec
-	{
-		//時間オーバー
-		workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
-	}
-	else
-	if(GW_NOW_DAM!=0)
+	if(GW_SKI_DOWN==3)		// 難易度ダウン３
 	{
-		//ダメージ
-		workG(GW_ENTRY_EVENT,SET,9)	//9=スキー失敗(ダメージ)
+		if(GW_NOW_BREAK>=16 && GW_NOW_DAM<=5 && SP003<3900)		//65秒=65*60sec
+		{
+			//達成できたらシルバー
+			workG(GW_ENTRY_EVENT,SET,2)		//シルバー
+		}
+		else
+		if(SP003>3900)						//65秒=65*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>5)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<12)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
+	if(GW_SKI_DOWN==2)		// 難易度ダウン２
 	{
-		//壊し足りない　ゼロ
-		workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		if(GW_NOW_BREAK>=26 && GW_NOW_DAM<=3 && SP003<3300)		//55秒=55*60sec
+		{
+			//達成できたらシルバー
+			workG(GW_ENTRY_EVENT,SET,2)		//シルバー
+		}
+		else
+		if(SP003>3300)						//55秒=55*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>3)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<22)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<32)
+	if(GW_SKI_DOWN==1)		// 難易度ダウン１
 	{
-		//壊し足りない　足りない
-		workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		if(GW_NOW_BREAK>=31 && GW_NOW_DAM<=1 && SP003<3000)		//50秒=50*60sec
+		{
+			//達成できたらシルバー
+			workG(GW_ENTRY_EVENT,SET,2)		//シルバー
+		}
+		else
+		if(SP003>3000)						//50秒=50*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>1)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<27)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
 	{
-		//壊し足りない　おしい
-		workG(GW_ENTRY_EVENT,SET,8)	//8=スキー失敗(ツボ、おしい)
+		if(GW_NOW_BREAK==36 && GW_NOW_DAM==0 && SP003<2700)		//45秒=45*60sec
+		{
+			//達成できたらシルバー
+			workG(GW_ENTRY_EVENT,SET,2)		//シルバー
+		}
+		else
+		if(SP003>2700)						//45秒=45*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM!=0)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<32)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 
 	//暗転
diff --git a/scp_jp_conv/map/0/EV00492.txt b/scp_conv/map/0/EV00492.txt
index 92c3133..e031221 100644
--- a/scp_jp_conv/map/0/EV00492.txt
+++ b/scp_conv/map/0/EV00492.txt
@@ -156,6 +156,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,78)	//攻略中ルート
 		workL(WK_ROUTETIME_STOP,SET,1)	// スコア計測停止
 
+		if(GW_SKI_COUNT3<255)
+		{
+			workG(GW_SKI_COUNT3,ADD,1)	//プレイ回数
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////ＨＰ0でも消えない　キャラ0は死亡時に"EV_DEAD"を再生
 		//ワープ封じ
 		workG(GW_WARP_FLAG,SET,0)//ワープ封じる。
@@ -303,41 +308,159 @@ EV_GOAL
 	SE(24,0)
 	CAM_Type(1)
 
-	if(GW_NOW_BREAK==21 && GW_NOW_DAM==0 && SP003<3600)
+	if(GW_SKI_DOWN==3)		// 難易度ダウン３
 	{
-		//達成できたらゴールド
-		workG(GW_ENTRY_EVENT,SET,3)	//ゴールド
+		if(GW_NOW_BREAK>=5 && GW_NOW_DAM<=5 && SP003<4200)
+		{
+			//達成できたらゴールド
+			workG(GW_ENTRY_EVENT,SET,3)		//ゴールド
+		}
+		else
+		if(SP003>4200)						//70秒=70*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>5)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<3)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(SP003>3600)		//60秒=60*60sec
+	if(GW_SKI_DOWN==2)		// 難易度ダウン２
 	{
-		//時間オーバー
-		workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		if(GW_NOW_BREAK>=13 && GW_NOW_DAM<=3 && SP003<3600)
+		{
+			//達成できたらゴールド
+			workG(GW_ENTRY_EVENT,SET,3)		//ゴールド
+		}
+		else
+		if(SP003>3600)						//60秒=60*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>3)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<11)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_DAM!=0)
+	if(GW_SKI_DOWN==1)		// 難易度ダウン１
 	{
-		//ダメージ
-		workG(GW_ENTRY_EVENT,SET,9)	//9=スキー失敗(ダメージ)
+		if(GW_NOW_BREAK>=17 && GW_NOW_DAM<=1 && SP003<3300)
+		{
+			//達成できたらゴールド
+			workG(GW_ENTRY_EVENT,SET,3)		//ゴールド
+		}
+		else
+		if(SP003>3300)						//55秒=55*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>1)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<15)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
 	{
-		//壊し足りない　ゼロ
-		workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
-	}
-	else
-	if(GW_NOW_BREAK<19)
-	{
-		//壊し足りない　足りない
-		workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
-	}
-	else
-	{
-		//壊し足りない　おしい
-		workG(GW_ENTRY_EVENT,SET,8)	//8=スキー失敗(ツボ、おしい)
+		if(GW_NOW_BREAK==21 && GW_NOW_DAM==0 && SP003<3000)
+		{
+			//達成できたらゴールド
+			workG(GW_ENTRY_EVENT,SET,3)		//ゴールド
+		}
+		else
+		if(SP003>3000)						//50秒=60*50sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM!=0)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<19)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 
+
+
 	//暗転
 	fade_in(100,60,0)
 	wait_fade()
diff --git a/scp_jp_conv/map/0/EV00493.txt b/scp_conv/map/0/EV00493.txt
index 79becb5..8e83a54 100644
--- a/scp_jp_conv/map/0/EV00493.txt
+++ b/scp_conv/map/0/EV00493.txt
@@ -39,11 +39,14 @@ INIT
 //	set_chr( 92,990,	-1,-1,    -55, 44200, -1500,	 0,6050, 6,"K2_16000;")	//エントリ 奈落
 //	set_chr( 93,990,	-1,-1,    107, 48800, -2500,	 0,6050, 6,"K2_16000;")	//エントリ 奈落
 	set_chr( 91,990,	-1,-1,    159, 55239,  -800,	 0,4010, 6,"<EV_GOAL>;")	//エントリ ゴール
-	set_chr( 92,990,	-1,-1,    -55, 44200, -1500,	 0,6050, 6,"<EV_FALL>;")	//エントリ 奈落
-	set_chr( 93,990,	-1,-1,    107, 48800, -2500,	 0,6050, 6,"<EV_FALL>;")	//エントリ 奈落
+	set_chr( 92,990,	-1,-1,    -55, 44200, -1400,	 0,6050, 6,"<EV_FALL>;")	//エントリ 奈落
+	set_chr( 93,990,	-1,-1,    107, 48800, -2400,	 0,6050, 6,"<EV_FALL>;")	//エントリ 奈落
 
 	set_chr( 94,990,	 0, 0,      0,      0,    0,	  0, 0 , 8,"(<EV_Snow> WT?50)")	//エフェクトループ再生用
 
+	set_chr( 95,991,	-1,-1,    -55, 44200, -1500,	 0,6050, 0,";")	//奈落の下のあたり
+	set_chr( 96,991,	-1,-1,    107, 48800, -2500,	 0,6050, 0,";")	//奈落の下のあたり
+
 //	set_chr( 90,990,	-1,-1,   -450,3000,-300,   	180,  1201,	6,"K9_10000;")	//①エントリ フィールド
 //	set_chr( 91,990,	-1,-1,   -100,-1330,0,  	330,050202,	6,"K0_16010;")	//①エントリ 入口分岐
 //	set_chr( 92,990,	-1,-1,   4950,-11700, 1850, 345,  1001,	6,"K0_16010;")	//①エントリ 坂上適当
@@ -128,6 +131,11 @@ INIT
 		workG(GW_NOW_ROUTE,SET,79)	//攻略中ルート
 		workL(WK_ROUTETIME_STOP,SET,1)	// スコア計測停止
 
+		if(GW_SKI_COUNT4<255)
+		{
+			workG(GW_SKI_COUNT4,ADD,1)	//プレイ回数
+		}
+
 		F_set_chr(PLAYER1,CF_NO_DEAD) ////ＨＰ0でも消えない　キャラ0は死亡時に"EV_DEAD"を再生
 
 		//ワープ封じ
@@ -327,7 +335,10 @@ EV_KappaWarp
 	SE(1016, KAPPA)	//ワ－プ
 	EFF_chr(24560,KAPPA,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA,-92,40991,3634,360,2)
+	if(GW_SKI_DOWN>=1)		// 難易度ダウン１
+		chr_pos(KAPPA,1562,43701,3493,360,2)
+	else
+		chr_pos(KAPPA,-92,40991,3634,360,2)
 }
 
 EV_KappaWarp1
@@ -351,7 +362,10 @@ EV_KappaWarp1
 	SE(1016, KAPPA)	//ワ－プ
 	EFF_chr(24560,KAPPA01,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA01,-406, 31210,  7999,360,2)
+	if(GW_SKI_DOWN>=1)		// 難易度ダウン１
+		chr_pos(KAPPA01,-1777,43442,3230,360,2)
+	else
+		chr_pos(KAPPA01,-406, 31210,7999,360,2)
 }
 
 EV_KappaWarp2
@@ -375,7 +389,10 @@ EV_KappaWarp2
 	SE(1016, KAPPA)	//ワ－プ
 	EFF_chr(24560,KAPPA02,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA02,-200,35814,5619,360,2)
+	if(GW_SKI_DOWN>=2)		// 難易度ダウン２
+		chr_pos(KAPPA02,-1777,43442,3230,360,2)
+	else
+		chr_pos(KAPPA02,-200,35814,5619,360,2)
 }
 
 EV_KappaWarp3
@@ -399,7 +416,10 @@ EV_KappaWarp3
 	SE(1016, KAPPA)	//ワ－プ
 	EFF_chr(24560,KAPPA03,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA03,91,34416,6413,360,2)
+	if(GW_SKI_DOWN>=2)		// 難易度ダウン２
+		chr_pos(KAPPA03,1562,43701,3493,360,2)
+	else
+		chr_pos(KAPPA03,91,34416,6413,360,2)
 }
 
 EV_KappaWarp4
@@ -430,7 +450,10 @@ EV_KappaWarp4
 	SE(1016, KAPPA)	//ワ－プ
 	EFF_chr(24560,KAPPA04,0,100,0,"charbase0")
 	wait(10)
-	chr_pos(KAPPA04,-92,40991,3634,360,2)
+	if(GW_SKI_DOWN>=3)		// 難易度ダウン３
+		chr_pos(KAPPA04,-1777,43442,3230,360,2)
+	else
+		chr_pos(KAPPA04,-92,40991,3634,360,2)
 }
 
 //--------------------------------------------------------------------
@@ -447,47 +470,183 @@ EV_GOAL
 	CAM_Type(1)
 
 	//-- 判定 -----------------------------------------------------------
-	if(F201)		// カッパゴール済み？
-	{
-		//カッパのほうが速かった
-		workG(GW_ENTRY_EVENT,SET,13)	//13=スキー失敗(カッパ)
-	}
-	else
-	if(GW_NOW_BREAK==16 && GW_NOW_DAM==0 && SP003<3000)
-	{
-		//達成できたらプラチナ
-		workG(GW_ENTRY_EVENT,SET,4)	//プラチナ
-	}
-	else
-	if(SP003>3000)		//50秒=50*60sec
-	{
-		//時間オーバー
-		workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
-	}
-	else
-	if(GW_NOW_DAM!=0)
+
+	if(GW_SKI_DOWN==3)		// 難易度ダウン３
 	{
-		//ダメージ
-		workG(GW_ENTRY_EVENT,SET,9)	//9=スキー失敗(ダメージ)
+		if(F201)							// カッパゴール済み？
+		{
+			//カッパのほうが速かった
+			workG(GW_ENTRY_EVENT,SET,13)	//13=スキー失敗(カッパ)
+		}
+		else
+		if(GW_NOW_BREAK>=6 && GW_NOW_DAM<=5 && SP003<4200)
+		{
+			//達成できたらプラチナ
+			workG(GW_ENTRY_EVENT,SET,4)		//プラチナ
+		}
+		else
+		if(SP003>4200)						//70秒=70*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>5)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<4)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<1)
+	if(GW_SKI_DOWN==2)		// 難易度ダウン２
 	{
-		//壊し足りない　ゼロ
-		workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		if(F201)							// カッパゴール済み？
+		{
+			//カッパのほうが速かった
+			workG(GW_ENTRY_EVENT,SET,13)	//13=スキー失敗(カッパ)
+		}
+		else
+		if(GW_NOW_BREAK>=11 && GW_NOW_DAM<=3 && SP003<3600)
+		{
+			//達成できたらプラチナ
+			workG(GW_ENTRY_EVENT,SET,4)		//プラチナ
+		}
+		else
+		if(SP003>3600)						//60秒=60*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>3)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<9)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
-	if(GW_NOW_BREAK<14)
+	if(GW_SKI_DOWN==1)		// 難易度ダウン１
 	{
-		//壊し足りない　足りない
-		workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		if(F201)							// カッパゴール済み？
+		{
+			//カッパのほうが速かった
+			workG(GW_ENTRY_EVENT,SET,13)	//13=スキー失敗(カッパ)
+		}
+		else
+		if(GW_NOW_BREAK>=14 && GW_NOW_DAM<=1 && SP003<3300)
+		{
+			//達成できたらプラチナ
+			workG(GW_ENTRY_EVENT,SET,4)		//プラチナ
+		}
+		else
+		if(SP003>3300)						//55秒=55*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM>1)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<12)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 	else
 	{
-		//壊し足りない　おしい
-		workG(GW_ENTRY_EVENT,SET,8)	//8=スキー失敗(ツボ、おしい)
+		if(F201)							// カッパゴール済み？
+		{
+			//カッパのほうが速かった
+			workG(GW_ENTRY_EVENT,SET,13)	//13=スキー失敗(カッパ)
+		}
+		else
+		if(GW_NOW_BREAK==16 && GW_NOW_DAM==0 && SP003<3000)
+		{
+			//達成できたらプラチナ
+			workG(GW_ENTRY_EVENT,SET,4)		//プラチナ
+		}
+		else
+		if(SP003>3000)						//50秒=50*60sec
+		{
+			//時間オーバー
+			workG(GW_ENTRY_EVENT,SET,10)	//10=スキー失敗(タイム)
+		}
+		else
+		if(GW_NOW_DAM!=0)
+		{
+			//ダメージ
+			workG(GW_ENTRY_EVENT,SET,9)		//9=スキー失敗(ダメージ)
+		}
+		else
+		if(GW_NOW_BREAK<1)
+		{
+			//壊し足りない　ゼロ
+			workG(GW_ENTRY_EVENT,SET,12)	//12=スキー失敗(ツボ、ゼロ)
+		}
+		else
+		if(GW_NOW_BREAK<14)
+		{
+			//壊し足りない　足りない
+			workG(GW_ENTRY_EVENT,SET,11)	//11=スキー失敗(ツボ、足りない)
+		}
+		else
+		{
+			//壊し足りない　おしい
+			workG(GW_ENTRY_EVENT,SET,8)		//8=スキー失敗(ツボ、おしい)
+		}
 	}
 
+
 	//暗転
 	fade_in(100,60,0)
 	wait_fade()
diff --git a/scp_jp_conv/map/0/EV00510.txt b/scp_conv/map/0/EV00510.txt
index 5d072a9..a348d48 100644
--- a/scp_jp_conv/map/0/EV00510.txt
+++ b/scp_conv/map/0/EV00510.txt
@@ -45,6 +45,36 @@ INIT
 //	set_obj("@ob00082a", 4, 3,     0,   0,  0,		270)						//③階段（墓場）
 	set_chr(192,1301,	 4, 3,     0,   0,  0,		  0,   270, 0,";")			//階段上（ダミー）
 
+//裏フィギュア館/パッチ用
+	if(!F6_11_GameClear)
+	{
+		set_obj2("mp00442",   6, 5, -450,-450,  0,	 0) //
+		set_obj2("mp00452",   6, 5,  450,-450,  0,	 0) //
+		set_obj2("mp00222",   6, 5, -450, 450,  0,	 0) //
+		set_obj2("mp00232",   6, 5,  450, 450,  0,	 0) //
+	}
+	else
+	{
+		set_obj2("mp00442",   6, 5, -450,-450,  0,	 0) //
+		set_obj2("mp00252",   6, 5,  450,-450,  0,	 0) //
+		set_obj2("mp00222",   6, 5, -450, 450,  0,	 0) //
+		set_obj2("mp00512",   6, 5,  450, 450,  0,	 0) //
+
+		set_obj2("mp00082",   7, 5, -450,-450,  0,	 0) //
+		set_obj2("mp00012",   7, 5,  450,-450,  0,	 0) //
+		set_obj2("mp00102",   7, 5, -450, 450,  0,	 0) //
+		set_obj2("mp00032",   7, 5,  450, 450,  0,	 0) //
+
+		set_chr( 93,990,	 7, 5,     0,   0,  0,		90,  0102, 6,"K0_10540;")	//③エントリ 博物館
+		set_obj("@ob00072a", 7, 5,     0,   0,  0,		90)						//③階段（Ｇコロ）
+		set_chr(193,1301,	 7, 5,     0,   0,  0,		  0,   270, 0,";")			//階段上（ダミー）
+
+		set_chr(87, 804,	 6,5,	 425,-200,0,	0,	0,	8,"(L2?99 [9991【フィギュア館 別室→】] WT?30 L2!99 [9903]);")	//案内
+		set_chr(88, 445,	 6,5,    300,-350,82,		2,   0, 3,";")//ギャランドゥ黄金像
+		set_chr(89, 991,	 6,5,    300,-350, 0,		0,0202, 0,";")//ギャランドゥ黄金像当たり
+
+	}
+
 	set_chr(100,990,	-1,-1,   11518,5426,0,		 90,  0101, 6,"RF100")	//
 	set_chr(101,990,	-1,-1,   11506,6298,0,		 90,  0101, 6,"RF100")	//
 	set_chr(102,990,	-1,-1,   11570,5872,0,		 90,  0407, 6,"SF100")	//受付　ロッテ
@@ -366,7 +396,32 @@ INIT
 
 	workG(GW_SKI_MODE,SET,0)	//ギブアップメニューをクリア
 
+	//NPCフィギュア宝箱発生イベントから
+	if(GW_ENTRY_EVENT==4)
+	{
+		workG(GW_ENTRY_EVENT,SET,0)
+		EV("EV_ALLGET_END")
+	}
+	else
 	//闘技場に挑戦して戻ってきたときのイベント
+	//▼サバイバル終了
+	if(GW_ENTRY_EVENT==3)
+	{
+		workG(GW_ENTRY_EVENT,SET,0)
+		F_reset_chr(PLAYER1,CF_NO_DEAD)
+		set_hp(PLAYER1,100)//全快
+
+		if(GW_WINLOSE==1)
+		{
+			EV("WIN_BATTLE3")
+		}
+		else
+		{
+			EV("LOSE_BATTLE")		//闘技場と同じだから内容に注意
+		}		
+	}
+	else
+	//▼闘技場
 	//すでにクリア済みのコースだった
 	if(GW_ENTRY_EVENT==2)
 	{
@@ -377,6 +432,7 @@ INIT
 		EV("WIN_BATTLE2")
 	}
 	else
+	//▼闘技場	
 	//初クリアだった．もしくは負け
 	if(GW_ENTRY_EVENT==1)
 	{
@@ -543,8 +599,9 @@ WIN_BATTLE
 	EV_end()
 }
 
-
+//──────────────────────────────
 //コースクリア２回目以降でアイテムを貰う処理。
+//──────────────────────────────
 WIN_BATTLE2
 {
 //　　闘技場受付、ロッテの前にフェードインする。
@@ -572,6 +629,7 @@ WIN_BATTLE2
 	MES(LOTTE,"おめでとうございます～。",0)
 	MES(LOTTE,"こちらが今回の\n賞品になりま～す。",0)
 	MES_close(LOTTE)
+	
 	EV("ITEMGET_SECOND")
 	wait_EV("ITEMGET_SECOND")
 
@@ -595,6 +653,60 @@ WIN_BATTLE2
 	EV_end()
 }
 
+//──────────────────────────────
+//サバイバルで勝利
+//──────────────────────────────
+WIN_BATTLE3
+{
+//　　闘技場受付、ロッテの前にフェードインする。
+	EV_begin()
+
+	//暗転
+	fade_in(100,1,0)
+	wait_fade()
+	wait(10)
+	
+	chr_pos(PLAYER2,11230,5753,0,270,2)
+	chr_pos(PLAYER1,11230,6011,0,270,2)
+	chr_pos(PET,11100,5883,0,270,2)
+	rot_chr(LOTTE,-1,PLAYER1)
+
+	//フェードイン
+	fade_in(0,60,0)
+	wait_fade()
+	wait(10)
+
+	MES(LOTTE,"おめでとうございます～。",0)
+	if(IT022>0)						//ペット「ペンギン」を既に持っている
+	{
+		MES(LOTTE,"見事に最後まで行きましたね～。\nこちらが今回の賞品になりま～す。",0)
+		MES_close(LOTTE)		
+		
+		SE(24,0)	//お金の音だと味気ない
+		MES(0,"C3５０万ペンネ受け取った。",2)
+		MES_close(0)
+		get_gold(500000,RAGNA)
+	}
+	else
+	{
+		MES(LOTTE,"見事に最後まで行きましたね～。\nこちらが今回の賞品になりま～す。",0)
+		MES_close(LOTTE)
+	
+		get_item(22,1,0)				//ペット「ペンギン」
+		wait_key(0)
+		menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+		menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+	}
+		
+	MES(LOTTE,"ヒマなら\nまた挑戦してくださいね～。",0)
+	MES_close(LOTTE)
+
+	EV("EV_WARP_FLAG")
+	wait_EV("EV_WARP_FLAG")
+
+	rot(LOTTE,30,90)
+	EV_end()
+}
 
 //──────────────────────────────
 //▼受付．敗北後の処理
@@ -1184,6 +1296,38 @@ EV_FIGURE_12
 	TK_end()
 }
 
+
+//---------------------------------------------------------------------
+//NPCフィギュアコンプリート
+EV_ALLGET
+{
+	if(!F1_05_FigureCmp)	//NPCフィギュアコンプリート
+	{
+		TK_begin()
+		wait(30)
+		F_set(F1_05_FigureCmp)
+		
+		fade_in(100,30,0)
+		wait_fade()
+		
+		workG(GW_ENTRY_EVENT,SET,4)
+		new_map(10540)
+	}
+}
+
+EV_ALLGET_END
+{	
+	chr_pos(RAGNA,   10194,5988,0,180,2)
+	chr_pos(PARTNER, 10105,6145,0,180,2)
+	chr_pos(PET,     10334,6145,0,180,2)
+
+	fade_in(0,30,0)
+	wait_fade()
+		
+	TK_end()
+}
+
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/0/EV00520.txt b/scp_conv/map/0/EV00520.txt
index 5f1934f..12cd719 100644
--- a/scp_jp_conv/map/0/EV00520.txt
+++ b/scp_conv/map/0/EV00520.txt
@@ -10,6 +10,8 @@
 
 #LOTTE		10
 
+//30～34は分身？
+
 /*
 #MAURICE	11
 #ODESSA		12
@@ -54,6 +56,7 @@
 
 //■ローカルワーク
 // 001:倒したザコの数
+// 002:サバイバルモードのとき1
 
 INIT
 {
@@ -72,147 +75,186 @@ INIT
 	//館内にいるよＬＦ。
 	F_set(90)
 
+	//▼カッパモード
+/*	if(GW_ENTRY_EVENT==3)
+	{
+		set_chr( 1,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 2,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 3,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 4,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 5,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 6,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 7,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 8,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+		set_chr( 9,311,		0,0,10280,10210,0,	0,	0,		0,";")//普通スライム
+//		set_chr( 10,350,	0,0,10280,10210,800,-1,	0,		8,"!F10 F1 F2 F3 F4 F5 F6 F7 F8 F9 S0_1 WT?120 V0_99;")//大スライム
+	
+	
+		EV("PRE_KAPPA_BATTLE")										//カッパ
+	}
+	else*/
+	
+	//▼サバイバル（カッパ後）
+	if(GW_ENTRY_EVENT==3)
+	{
+		workG(GW_ENTRY_EVENT,SET,3)							//終了後の分岐に使用
+		EV("PRE_SURVIVAL_LOOP")
+		wait_EV("PRE_SURVIVAL_LOOP")
+		
+		
+	}
+	else
+	//▼サバイバル	
+	if(GW_ENTRY_EVENT==2)
+	{
+		workG(GW_ENTRY_EVENT,SET,3)							//終了後の分岐に使用
+		EV("PRE_SURVIVAL")									//サバイバル
+	}
 	//▼闘技場
-	if(GW_ENTRY_EVENT==1)
+	else
 	{
-//必ず本戦から始まるように修正 2008.07.29. 18:40
-		workG(GW_SKI_MODE,SET,5)	//ギブアップメニューをセット
+	
+		if(GW_ENTRY_EVENT==1)
+		{
+	//必ず本戦から始まるように修正 2008.07.29. 18:40
+			workG(GW_SKI_MODE,SET,5)	//ギブアップメニューをセット
 
-		set_chr( LOTTE,1068,	-1,-1,  10388,10356,1,	0,0,0,"")	//　ロッテ
-		MOT_SET( LOTTE,159,159,3001,3061,-1,-1 )
-		MOT(LOTTE,159,0)
+			set_chr( LOTTE,1068,	-1,-1,  10388,10356,1,	0,0,0,"")	//　ロッテ
+			MOT_SET( LOTTE,159,159,3001,3061,-1,-1 )
+			MOT(LOTTE,159,0)
 
-		//バトルに挑戦するのが初回の場合、演出を見せる初期位置に
-		if(GW_TRY_CUP==1)
-		{
-			if(!FV_FF_BAMaurice)
+			//バトルに挑戦するのが初回の場合、演出を見せる初期位置に
+			if(GW_TRY_CUP==1)
 			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAMaurice)
+				if(!FV_FF_BAMaurice)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAMaurice)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==2)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==2)
-		{
-			if(!FV_FF_BAOdessa)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAOdessa)
+				if(!FV_FF_BAOdessa)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAOdessa)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==3)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==3)
-		{
-			if(!FV_FF_BAPockle)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAPockle)
+				if(!FV_FF_BAPockle)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAPockle)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==4)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==4)
-		{
-			if(!FV_FF_BAPipiro)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAPipiro)
+				if(!FV_FF_BAPipiro)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAPipiro)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==5)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==5)
-		{
-			if(!FV_FF_BASubaru)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BASubaru)
+				if(!FV_FF_BASubaru)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BASubaru)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==6)
 			{
-				F_reset(FV_FF_FarstBattle)
-			}
-		}
-		else
-		if(GW_TRY_CUP==6)
-		{
-			if(!FV_FF_BAFiona)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAFiona)
+				if(!FV_FF_BAFiona)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAFiona)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==7)
 			{
-				F_reset(FV_FF_FarstBattle)
+				if(!FV_FF_BAKlode)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAKlode)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
-		}
-		else
-		if(GW_TRY_CUP==7)
-		{
-			if(!FV_FF_BAKlode)
+			else
+			if(GW_TRY_CUP==8)
 			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAKlode)
+				if(!FV_FF_BAGyarandow)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAGyarandow)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 			else
+			if(GW_TRY_CUP==9)
 			{
-				F_reset(FV_FF_FarstBattle)
+				if(!FV_FF_BAPenguin)
+				{
+					F_set(FV_FF_FarstBattle)
+					F_set(FV_FF_BAPenguin)
+				}
+				else
+				{
+					F_reset(FV_FF_FarstBattle)
+				}
 			}
 		}
-		else
-		if(GW_TRY_CUP==8)
+
+		if(FV_FF_FarstBattle)
 		{
-			if(!FV_FF_BAGyarandow)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAGyarandow)
-			}
-			else
-			{
-				F_reset(FV_FF_FarstBattle)
-			}
+			//初回の処理
+			EV("PRE_BATTLE")
 		}
+		//そうでない場合は最初から敵と向き合っている
 		else
-		if(GW_TRY_CUP==9)
 		{
-			if(!FV_FF_BAPenguin)
-			{
-				F_set(FV_FF_FarstBattle)
-				F_set(FV_FF_BAPenguin)
-			}
-			else
-			{
-				F_reset(FV_FF_FarstBattle)
-			}
+		//2回目以降の処理
+			EV("PRE_BATTLE_2")
 		}
-	}
 
-	if(FV_FF_FarstBattle)
-	{
-		//初回の処理
-		EV("PRE_BATTLE")
 	}
-	//そうでない場合は最初から敵と向き合っている
-	else
-	{
-	//2回目以降の処理
-		EV("PRE_BATTLE_2")
-	}
-
 	map_color(85,80,80,0);//R,G,B, time 100%
 }
 
@@ -1026,8 +1068,10 @@ PRE_BATTLE
 
 			if(!F4_09_GoShrineMia)
 			{
-				KAO(ENEMY_CHARA, "B232BZ6", "1233321", "5")	
-				MES(ENEMY_CHARA,"あ、あの僕、\nこの後フィオナさんに\n頼まれてる調査があって……",0)
+//				KAO(ENEMY_CHARA, "B232BZ6", "1233321", "5")		//※村で通用しないため下と合わせた（竹0922）
+//				MES(ENEMY_CHARA,"あ、あの僕、\nこの後フィオナさんに\n頼まれてる調査があって……",0)
+				KAO(ENEMY_CHARA, "B232BZ4", "1233321", "5")	
+				MES(ENEMY_CHARA,"あ、あの僕、今は\nちょっと忙しいんですけどっ……",0)
 				MES_close(ENEMY_CHARA)
 			}
 			else
@@ -1790,34 +1834,49 @@ EV_DEAD
 	wait_BGM()
 
 	//-- 負けて受付に戻る ------------------------------------------------
-
-	if(GW_TRY_CHARA==0)
+	if(WK002==1)		//WK002が1ならサバイバルモード
 	{
-		join_party(1)//ALWENをパーティーに戻す
-		
-		//フィギュアゲット
-		if(!F2857)
+		if(GW_TRY_CHARA==0)
 		{
-			SE(24,0)//ゲットSE
-			MES(0,"L777参加賞として、\nL667ラグナL777のフィギュアを手に入れた！！",2)
-			MES_close(0)
-			F_set(2857)
+			join_party(1)//ALWENをパーティーに戻す
 		}
+		else
+		{
+			join_party(0)//RAGNAをパーティーに戻す		
+		}	
+		workL(002,SET,0)
 	}
 	else
 	{
-		join_party(0)//RAGNAをパーティーに戻す
-		
-		//フィギュアゲット
-		if(!F2858)
+	
+		if(GW_TRY_CHARA==0)
 		{
-			SE(24,0)//ゲットSE
-			MES(0,"L777参加賞として、\nL667アルウェンL777のフィギュアを手に入れた！！",2)
-			MES_close(0)
-			F_set(2858)
+			join_party(1)//ALWENをパーティーに戻す
+			
+			//フィギュアゲット
+			if(!F2857)
+			{
+				SE(24,0)//ゲットSE
+				MES(0,"L777参加賞として、\nL667ラグナL777のフィギュアを手に入れた！！",2)
+				MES_close(0)
+				F_set(2857)
+			}
+		}
+		else
+		{
+			join_party(0)//RAGNAをパーティーに戻す
+			
+			//フィギュアゲット
+			if(!F2858)
+			{
+				SE(24,0)//ゲットSE
+				MES(0,"L777参加賞として、\nL667アルウェンL777のフィギュアを手に入れた！！",2)
+				MES_close(0)
+				F_set(2858)
+			}
 		}
+	
 	}
-
 	wait(15)
 	CAM_return( 0 )
 	new_map(10510)
@@ -2988,7 +3047,7 @@ ITEMGET_FIRST	//
 		wait(20)
 		fade_in(30,10,BLACK)		//少し暗転
 
-		if(IT113>0)
+		if(IT113>=0)
 			get_item(196,1,0)
 		else
 			get_item(113,1,0)
@@ -3108,7 +3167,7 @@ ITEMGET_FIRST	//
 		wait(20)
 		fade_in(30,10,BLACK)		//少し暗転
 
-		if(IT116>0)
+		if(IT116>=0)
 		{
 			get_item(166,1,0)
 			wait(70)
@@ -3157,15 +3216,22 @@ ITEMGET_FIRST	//
 		fade_in(30,10,BLACK)		//少し暗転
 
 		if(IT138>0)
-			get_item(182,1,0)
-		else
-			get_item(138,1,0)
+			get_item(182,1,0)		//パイナップル
+		else	
+			get_item(138,1,0)		//レベルプレートＧ
 		wait(70)
 		wait_key(0)
+		menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+		menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)		
+		
+		SE(043,PLAYER1)
+MES_pos(0,"C3『レベルプレートＧ』はダンジョン内にある\nレベルプレートを調べることで使用します。\n敵は通常より強くなりますが、\nアイテムの出現確率や一部の宝箱の中身が変化します。",2,120,200,400,100)	
+		wait_key(0)	
+		MES_close(0)		
+		
 		BGM_vol(100,30)				//BGM戻し
 		fade_in(0,10,BLACK)			//暗転解除
-		menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
-		menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+
 		
 		//フィギュアゲット
 		if(!F2848)
@@ -4142,5 +4208,390 @@ DELETE_ROPE
 }
 
 
+
+//──────────────────────────────
+//サバイバルモード
+//──────────────────────────────
+PRE_SURVIVAL
+{
+
+	workG(GW_TRY_CUP,SET,1)
+//	workG(GW_TRY_CUP,SET,6)
+	workL(002,SET,1)
+	set_hp(PLAYER1,100)//全快	
+		
+	EV("PRE_SURVIVAL_LOOP")
+	wait_EV("PRE_SURVIVAL_LOOP")
+}
+
+//──────────────────────────────
+// サバイバル（初回）
+//──────────────────────────────
+PRE_SURVIVAL_FIRST
+{
+	//――――――――――――――――――――――――――
+	//	初期化処理
+	//――――――――――――――――――――――――――
+	//暗転
+//	fade_in(100,1,0)
+//	wait_fade()
+//	wait(1)
+
+//	EV("PRE_BATTLE_SET")
+//	wait_EV("PRE_BATTLE_SET")
+
+	chr_pos(PLAYER1,	10651,10772,1,90,2)
+	color(ENEMY_CHARA,	-1)	//透過
+	color(PLAYER1,		-1)		//透過
+	color(PLAYER2,		-1)		//透過
+	color(LOTTE,		1)		//
+
+	set_chr( LOTTE,1068,	-1,-1,  10388,10356,1,	0,0,0,"")	//　ロッテ		
+	chr_equip2( LOTTE,"eq_062", "Bone_LeftHand", 100,	90,0,0,	-7,0,2);
+
+	wait(30)
+
+	//カメラセット
+	CAM_move(10388,-10456,162,0,0)
+	CAM(-50,118,162,20,180,0,0)
+	CAM_move(10388,-10456,162,100,0)
+	CAM(-50,50,162,21,180,100,0)
+
+	fade_in( 0, 60, BLACK)	//フェードイン
+	wait_fade()
+
+
+	if( GW_TRY_CUP==6)
+	{
+		KAO(LOTTE,"52625Z4","5","6")	
+		MES(LOTTE,"P1S4さぁ、張り切って後半戦いってみましょ～！",0)
+		MES_close(LOTTE)
+		wait_MES(LOTTE)			
+	}
+	else
+	{
+		CAM_quake("463746")
+		KAO(LOTTE,"52625Z4","5","6")
+		MES(LOTTE,"P1S4レディース＆ジェントルメ～ン！",0)
+		KAO(LOTTE,"52625Z3","321","6")
+		MES(LOTTE,"P1S4お待たせしました～。",0)
+		KAO(LOTTE,"52625Z6","1","6")
+		MES(LOTTE,"P1S4今宵はサバイバル戦を執り行いま～す！",0)
+		KAO(LOTTE,"52625Z6","1236","6")		
+		MES(LOTTE,"P1S4さぁ、ノンストップバトルの始まりで～す！！",0)
+		MES_close(LOTTE)
+		wait_MES(LOTTE)	
+	}
+
+
+	SE(591,0)//歓声
+	
+	//暗転
+	fade_in(100,30,0)
+	wait_fade()
+
+}
+
+//──────────────────────────────
+// サバイバル（ループ）
+//──────────────────────────────
+PRE_SURVIVAL_LOOP
+{
+	EV_begin()
+
+	workG(GW_SKI_MODE,SET,5)	//ギブアップメニューをセット
+
+	//暗転
+	fade_in(100,1,0)
+	wait_fade()
+	wait(1)
+
+	if(GW_TRY_CUP==1 || GW_TRY_CUP==6)
+	{
+		//初回限定
+		EV("PRE_SURVIVAL_FIRST")
+		wait_EV("PRE_SURVIVAL_FIRST")
+	}
+
+
+	//対戦相手を設定する
+	if(GW_TRY_CUP==1)
+	{
+		set_chr( ENEMY_CHARA,390,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：モーリス
+		workG(GW_TRY_CHARA,SET,0)										//対戦者　：ラグナ
+		chr_state_LV( ENEMY_CHARA, 26 )									//敵レベル設定(初期4)	chr_state_LV は 加算
+		chr_state_LV( ENEMY_CHARA, 30)					
+	}
+	else
+	if(GW_TRY_CUP==2)
+	{
+		set_chr( ENEMY_CHARA,392,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：オデッサ
+		workG(GW_TRY_CHARA,SET,1)										//対戦者　：アルウェン
+		chr_state_LV( ENEMY_CHARA, 23 )									//敵レベル設定(初期7)		
+		chr_state_LV( ENEMY_CHARA, 30)					
+	}
+	else
+	if(GW_TRY_CUP==3)
+	{
+		set_chr( ENEMY_CHARA,396,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：ポックル
+		workG(GW_TRY_CHARA,SET,0)										//対戦者　：ラグナ
+		chr_state_LV( ENEMY_CHARA, 28 )									//敵レベル設定(初期12)
+		chr_state_LV( ENEMY_CHARA, 20)			
+	}
+	else
+	if(GW_TRY_CUP==4)
+	{
+		set_chr( ENEMY_CHARA,397,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：ピピロ
+		workG(GW_TRY_CHARA,SET,1)										//対戦者　：アルウェン
+		chr_state_LV( ENEMY_CHARA, 17)									//敵レベル設定(初期13)
+		chr_state_LV( ENEMY_CHARA, 20)			
+	}	
+	else
+	if(GW_TRY_CUP==5)
+	{
+		set_chr( ENEMY_CHARA,391,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：スバル
+		workG(GW_TRY_CHARA,SET,1)										//対戦者　：アルウェン
+		chr_state_LV( ENEMY_CHARA, 13)									//敵レベル設定(初期17)
+		chr_state_LV( ENEMY_CHARA, 30)	
+	}
+	else	
+	if(GW_TRY_CUP==6)
+	{
+		set_chr( ENEMY_CHARA,393,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：フィオナ
+		workG(GW_TRY_CHARA,SET,1)										//対戦者　：アルウェン
+		chr_state_LV( ENEMY_CHARA, 10 )									//敵レベル設定(初期20)
+		chr_state_LV( ENEMY_CHARA, 5 )									//
+	}	
+	else
+	if(GW_TRY_CUP==7)
+	{
+		set_chr( ENEMY_CHARA,394,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：クロード
+		workG(GW_TRY_CHARA,SET,0)										//対戦者　：ラグナ
+		chr_state_LV( ENEMY_CHARA, 7)									//敵レベル設定(初期23)
+		chr_state_LV( ENEMY_CHARA, 15 )			
+	}	
+	else
+	if(GW_TRY_CUP==8)
+	{
+		set_chr( ENEMY_CHARA,398,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：ギャランドゥ
+		workG(GW_TRY_CHARA,SET,0)										//対戦者　：ラグナ
+		chr_state_LV( ENEMY_CHARA, 3)									//敵レベル設定(初期27)
+		chr_state_LV( ENEMY_CHARA, 10 )			
+	}	
+	else
+	if(GW_TRY_CUP==9)
+	{
+		set_chr( ENEMY_CHARA,399,	-1,-1,  9501,8247,1,	2,0,0,"")	//対戦相手：ペンギン
+		workG(GW_TRY_CHARA,SET,1)										//対戦者　：アルウェン
+		chr_state_LV( ENEMY_CHARA, 10 )									//敵レベル設定(初期30)
+		chr_state_LV( ENEMY_CHARA, 10 )									//
+	}	
+
+
+
+	F_set_chr(PLAYER1,CF_NO_DEAD) ////ＨＰ0でも消えない　キャラ0は死亡時に"EV_DEAD"を再生
+
+	set_chr( ZAKO_19,990,	-1,-1,  11388,9309,1,	10,0,8,"(F9 <EV_WIN_SURVIVAL> RF9)")
+	F_set_chr(ENEMY_CHARA,CF_NO_DEAD)
+	F_set_chr(ENEMY_CHARA,CF_NO_DROPITEM)
+	
+	color(ENEMY_CHARA,1)	//
+
+	//パーティを一人にする。(※パーティに２人いること前提)
+	if(GW_TRY_CHARA==0)
+	{
+		clear_party(PARTNER)	//アルウェン消去
+//		delete(PLAYER2)	
+		color(PLAYER2,-1)
+		color(PLAYER1, 1)
+	}
+	else
+	{
+		clear_party(99)			//アルウェンのみの操作モードへ	
+//		delete(RAGNA)			//これやると、スバルの分身時に不具合発生
+		color(PLAYER2,-1)
+		color(PLAYER1, 1)
+	}
+
+	chr_pos(PLAYER1,	10651,10772,1,90,2)
+//	chr_pos(PLAYER2,	10651,10772,1,90,2)
+	chr_pos(PLAYER2,	0,0,1,90,2)
+	
+	KAO(PLAYER1, "1", "1", "1")
+	KAO(LOTTE, "1", "1", "1")
+
+
+	EV("SET_ROPE")												//ロープセット
+
+	//初期位置セット 2戦目以降
+	chr_pos(PLAYER1,	10651,10772,1,90,2)
+	chr_pos(ENEMY_CHARA,	10120,10772,1,270,2)
+
+
+	CAM_move(10388,-10676,102,0,0)
+	CAM(950,183,102,21,180,0,0)
+	CAM_move(10388,-10456,122,120,0)
+	CAM(-50,107,122,22,180,120,0)
+
+	SE(591,0)//歓声
+	KAO(LOTTE,"1","1","3")
+
+
+
+	fade_in( 0, 60, BLACK)	//フェードイン
+	wait_CAM()
+	wait_CAM_move()
+	wait_fade()
+
+
+	//名前を画面に表示
+	if(GW_TRY_CUP==1)
+		set_namebmp(34,0)	//やる気中年モーリス	Ｇ－コロッセオ
+	if(GW_TRY_CUP==2)
+		set_namebmp(35,0)	//餓狼狩りオデッサ		Ｇ－コロッセオ
+	if(GW_TRY_CUP==3)
+		set_namebmp(37,0)	//純情少年ポックル		Ｇ－コロッセオ
+	if(GW_TRY_CUP==4)
+		set_namebmp(38,0)	//魔法少女ピピロ		Ｇ－コロッセオ
+	if(GW_TRY_CUP==5)
+		set_namebmp(36,0)	//見習い忍者スバル		Ｇ－コロッセオ
+	if(GW_TRY_CUP==6)	
+		set_namebmp(39,0)	//聖剣使いフィオナ		Ｇ－コロッセオ
+	if(GW_TRY_CUP==7)
+		set_namebmp(40,0)	//戦闘執事クロード		Ｇ－コロッセオ
+	if(GW_TRY_CUP==8)
+		set_namebmp(41,0)	//覆面超人ギャランドゥ	Ｇ－コロッセオ
+	if(GW_TRY_CUP==9)
+		set_namebmp(42,0)	//絶対究極無敵ペンギン	Ｇ－コロッセオ
+	wait(90)
+
+//　　同時に両者ＳＥつきで構える。
+	EV("KAMAE_SET")
+	wait_EV("KAMAE_SET")
+
+
+	EFF(21630,320,240,0,0,100,0)//FIGHT
+	wait(40)
+	SE(211,PLAYER1)
+	EV("PLAY_VOICE_Fight")
+
+	//構えを戻す
+	EV("KAMAE_RESET")
+	wait_EV("KAMAE_RESET")
+
+	//ロッテをどかす
+	if(GW_TRY_CUP==1 || GW_TRY_CUP==6)
+	{
+		//初回限定
+		MOT(LOTTE,153,2)
+		rot(LOTTE,60,360)
+		KAO(LOTTE,"5","5","6")
+		jump(LOTTE,0,20,9549,9099,0,400)
+	}
+
+	CAM_return( 30 )
+
+	workL(WK_BOSSHP,SET,ENEMY_CHARA)	//BOSS＿ＨＰ表示
+	BGM(45)
+	EV_end()
+
+	//ペット消す
+	color(PET,-1)
+
+	//戦闘開始
+
+
+}
+
+
+
+//──────────────────────────────
+//サバイバルで１つの試合に勝利
+EV_WIN_SURVIVAL
+{
+	delete(ZAKO_19)	// 判定キャラ消去
+	delete(30)	// 分身キャラ消去
+	delete(31)	// 
+	delete(32)	// 
+	delete(33)	// 
+	delete(34)	// 
+	
+	DelDropItem()	//ドロップアイテム全消し
+	StopEffect()	//エフェクト全消し
+
+	map_color(100,100,100, 5);//R,G,B, time 100%
+	map_specular(80,80,80, 5);//R,G,B, time 100%
+
+	EV_begin()
+	wait(20)
+	map_specular(0,0,0,20);//R,G,B, time 100%
+	KAO(ENEMY_CHARA,"5","5","5")//死亡用フェイスセット0822
+	wait(30)
+	
+	EV("PLAY_VOICE_EnemyLose")
+	CAM_move_chr(ENEMY_CHARA,90,0)
+	rot_chr(PLAYER1,30,ENEMY_CHARA)	
+	
+	
+	EFF(21650,320,240,0,0,100,0)//WIN
+	wait(60)
+	rot_chr(PLAYER1,30,ENEMY_CHARA)
+
+	wait(30)
+
+	wait(30)
+	fade_in(100,60,0)
+	wait(60)
+	wait_CAM_move()
+//	wait_BGM()
+	wait_EV("PLAY_VOICE_EnemyLose")
+	wait_fade()
+
+	
+	delete(ENEMY_CHARA)
+	
+	
+	//いないほうのキャラを加え、２人組みに戻す
+	if(GW_TRY_CHARA==0)
+	{
+		join_party(1)			//ラグナ
+	}
+	else
+	{
+		join_party(0)			//アルウェン
+	}	
+	
+	//▼最後の試合だった
+	if(GW_TRY_CUP==9)
+	{
+		workG(GW_ENTRY_EVENT,SET,3)
+		workG(GW_WINLOSE,SET,1)		//勝ったGWを立てる
+		F_set(FV_FF_WinSurvival)	//★闘技場サバイバルに勝った
+		stop_BGM(60)		
+		workL(002,SET,0)
+		new_map(10510)				//Ｇコロに戻る
+	}
+	else
+	//▼カッパへ
+	if(GW_TRY_CUP==5)
+//	if(GW_TRY_CUP==1)				//カッパ直前の試合だった
+	{
+		workG(GW_TRY_CUP,SET,6)		//次の試合へ　カッパ後の試合番号
+//		workG(GW_TRY_CUP,SET,9)		//次の試合へ　カッパ後の試合番号		
+		stop_BGM(60)	
+		new_map(10521)				
+	}
+	//▼次の試合へ
+	else
+	{
+		workG(GW_TRY_CUP,ADD,1)	//次の試合へ
+	
+//		workG(GW_TRY_CUP,SET,7)	//強制ペンぎん
+		EV("PRE_SURVIVAL_LOOP")
+	}
+
+}
+
+
 #EndScriptTable
 //====================================================================
diff --git a/scp_jp_conv/map/0/EV00530.txt b/scp_conv/map/0/EV00530.txt
index a776aa6..82d1721 100644
--- a/scp_jp_conv/map/0/EV00530.txt
+++ b/scp_conv/map/0/EV00530.txt
@@ -7,6 +7,9 @@
 
 #GATEROPE	1
 
+#TREASURE_CH	60
+#IT_TREASURE	32	//◇デモンジャケット
+
 INIT
 {
 //  -------  no typ   	  tip      x    y   z       mot     向 状  000+++++++010+++++++020+++++++030+++++++040+++++++050+++++++060+++++++070+++++++080+++++++090+++++++100+++++++110+++++++120+++++++130+++++++140+++++++150+++++++160+++++++170+++++++180+++++++190+++++++200+++++++210+++++++220+++++++230+++++++240+++++++250++
@@ -38,6 +41,9 @@ INIT
 	set_chr(99, 991,	-1,-1,6208,12678,0,		0,0202,0,";")//ギャランドゥ黄金像当たり
 
 
+	if(F6_11_GameClear)
+		set_chr( 250,648,	 3, 7,     0,   0,  0,		0,	0, 0,";")	//①レベルプレート
+
 //――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 //	■ボス再戦。
 //	勝利時に立てるフラグは以下のとおり。
@@ -70,7 +76,10 @@ INIT
 	}
 	else
 	{
-		set_chr(11, 760,  3,5,	-100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_01>")//760	ボスゲーム筐体
+		if(F3100)//ハードクリア
+			set_chr(11, 773,  3,5,	-100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_01>")//760	ボスゲーム筐体
+		else
+			set_chr(11, 760,  3,5,	-100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_01>")//760	ボスゲーム筐体
 	}
 
 	//水魔エフェメルガ戦	->Figure F2835
@@ -81,7 +90,10 @@ INIT
 	}
 	else
 	{
-		set_chr(12, 760,  3,5,	 300,  -350,	000,	0,0,2,"<EV_BOSS_GAME_02>")//760	ボスゲーム筐体
+		if(F3101)//ハードクリア
+			set_chr(12, 773,  3,5,	 300,  -350,	000,	0,0,2,"<EV_BOSS_GAME_02>")//760	ボスゲーム筐体
+		else
+			set_chr(12, 760,  3,5,	 300,  -350,	000,	0,0,2,"<EV_BOSS_GAME_02>")//760	ボスゲーム筐体
 	}
 	
 	//妖花アビスフラワー戦	->Figure F2834
@@ -92,7 +104,10 @@ INIT
 	}
 	else
 	{
-		set_chr(13, 760,  3,5,	 700,  -350,	000,	0,0,2,"<EV_BOSS_GAME_03>")//760	ボスゲーム筐体
+		if(F3102)//ハードクリア
+			set_chr(13, 773,  3,5,	 700,  -350,	000,	0,0,2,"<EV_BOSS_GAME_03>")//760	ボスゲーム筐体
+		else
+			set_chr(13, 760,  3,5,	 700,  -350,	000,	0,0,2,"<EV_BOSS_GAME_03>")//760	ボスゲーム筐体
 	}
 	
 	//火竜ファブニール戦	->Figure F2838	->Figure F2880
@@ -106,7 +121,10 @@ INIT
 	}
 	else
 	{
-		set_chr(14, 760,  3,5,	1125,  -350,	000,	0,0,2,"<EV_BOSS_GAME_04>")//760	ボスゲーム筐体
+		if(F3103)//ハードクリア
+			set_chr(14, 773,  3,5,	1125,  -350,	000,	0,0,2,"<EV_BOSS_GAME_04>")//760	ボスゲーム筐体
+		else
+			set_chr(14, 760,  3,5,	1125,  -350,	000,	0,0,2,"<EV_BOSS_GAME_04>")//760	ボスゲーム筐体
 
 		//------FIGURE------------
 		if(F2880)
@@ -135,7 +153,10 @@ INIT
 	}
 	else
 	{
-		set_chr(16, 765,  3,5,	1800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_06>")//760	ボスゲーム筐体
+		if(F3104)//ハードクリア
+			set_chr(16, 774,  3,5,	1800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_06>")//760	ボスゲーム筐体
+		else
+			set_chr(16, 765,  3,5,	1800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_06>")//760	ボスゲーム筐体
 
 		//------FIGURE------------
 		if(F2881)
@@ -157,7 +178,10 @@ INIT
 	}
 	else
 	{
-		set_chr(17, 765,  3,5,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_07>")//760	ボスゲーム筐体
+		if(F3105)//ハードクリア
+			set_chr(17, 774,  3,5,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_07>")//760	ボスゲーム筐体
+		else
+			set_chr(17, 765,  3,5,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_07>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2882)
 		{
@@ -181,7 +205,10 @@ INIT
 	}
 	else
 	{
-		set_chr(18, 765,  3,5,	3100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_08>")//760	ボスゲーム筐体
+		if(F3106)//ハードクリア
+			set_chr(18, 774,  3,5,	3100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_08>")//760	ボスゲーム筐体
+		else
+			set_chr(18, 765,  3,5,	3100,  -350,	000,	0,0,2,"<EV_BOSS_GAME_08>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2883)
 		{
@@ -202,7 +229,10 @@ INIT
 	}
 	else
 	{
-		set_chr(15, 760,  3,5,	3750,  -350,	000,	0,0,2,"<EV_BOSS_GAME_05>")//760	ボスゲーム筐体
+		if(F3107)//ハードクリア
+			set_chr(15, 773,  3,5,	3750,  -350,	000,	0,0,2,"<EV_BOSS_GAME_05>")//760	ボスゲーム筐体
+		else
+			set_chr(15, 760,  3,5,	3750,  -350,	000,	0,0,2,"<EV_BOSS_GAME_05>")//760	ボスゲーム筐体
 	}
 
 	//ダークアルウェン戦	->Figure F2884
@@ -216,7 +246,10 @@ INIT
 	}
 	else
 	{
-		set_chr(19, 765,  3,6,	 550,  -350,	000,	0,0,2,"<EV_BOSS_GAME_09>")//760	ボスゲーム筐体
+		if(F3108)//ハードクリア
+			set_chr(19, 774,  3,6,	 550,  -350,	000,	0,0,2,"<EV_BOSS_GAME_09>")//760	ボスゲーム筐体
+		else
+			set_chr(19, 765,  3,6,	 550,  -350,	000,	0,0,2,"<EV_BOSS_GAME_09>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2884)
 		{
@@ -242,7 +275,10 @@ INIT
 	}
 	else
 	{
-		set_chr(20, 760,  3,6,	1250,  -350,	000,	0,0,2,"<EV_BOSS_GAME_10>")//760	ボスゲーム筐体
+		if(F3109)//ハードクリア
+			set_chr(20, 773,  3,6,	1250,  -350,	000,	0,0,2,"<EV_BOSS_GAME_10>")//760	ボスゲーム筐体
+		else
+			set_chr(20, 760,  3,6,	1250,  -350,	000,	0,0,2,"<EV_BOSS_GAME_10>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2885)
 		{
@@ -266,8 +302,14 @@ INIT
 	}
 	else
 	{
-		set_chr(21, 760,  3,6,	1950,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_01>")//760	ボスゲーム筐体
-		set_chr(21, 760,  3,6,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_02>")//760	ボスゲーム筐体
+		if(F3110)//ハードクリア
+			set_chr(21, 773,  3,6,	1950,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_01>")//760	ボスゲーム筐体
+		else
+			set_chr(21, 760,  3,6,	1950,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_01>")//760	ボスゲーム筐体
+		if(F3111)//ハードクリア
+			set_chr(21, 773,  3,6,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_02>")//760	ボスゲーム筐体
+		else
+			set_chr(21, 760,  3,6,	2450,  -350,	000,	0,0,2,"<EV_BOSS_GAME_11_02>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2886)
 		{
@@ -291,7 +333,10 @@ INIT
 	}
 	else
 	{
-		set_chr(22, 760,  3,6,	2800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_12>")//760	ボスゲーム筐体
+		if(F3112)//ハードクリア
+			set_chr(22, 773,  3,6,	2800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_12>")//760	ボスゲーム筐体
+		else
+			set_chr(22, 760,  3,6,	2800,  -350,	000,	0,0,2,"<EV_BOSS_GAME_12>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2887)
 		{
@@ -310,8 +355,14 @@ INIT
 	}
 	else
 	{
-		set_chr(23, 760,  3,6,	5150,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_01>")//760	ボスゲーム筐体
-		set_chr(23, 760,  3,6,	5650,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_02>")//760	ボスゲーム筐体
+		if(F3113)//ハードクリア
+			set_chr(23, 773,  3,6,	5150,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_01>")//760	ボスゲーム筐体
+		else
+			set_chr(23, 760,  3,6,	5150,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_01>")//760	ボスゲーム筐体
+		if(F3114)//ハードクリア
+			set_chr(23, 773,  3,6,	5650,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_02>")//760	ボスゲーム筐体
+		else
+			set_chr(23, 760,  3,6,	5650,  -350,	000,	0,0,2,"<EV_BOSS_GAME_13_02>")//760	ボスゲーム筐体
 		//------FIGURE------------
 		if(F2888)
 		{
@@ -324,6 +375,26 @@ INIT
 		//------------------------
 	}
 
+
+//■宝箱配置────────────────────────────────────────────────────────────
+	workL(001,SET,0)
+	if(F3100 && F3101 && F3102 && F3103 && F3104 && F3105 && F3106 && F3107 )	
+		workL(001,ADD,1)
+	if(F3108 && F3109 && F3110 && F3111 && F3112 && F3113 && F3114 )	
+		workL(001,ADD,1)
+
+	if(WK001==2)
+	{
+		if(IT_TREASURE<1)
+			set_chr( TREASURE_CH,563,	 3,7,    -400, 0,  0,	6,   270,20,"<TK_PARTGG>;")	//①宝箱（並）
+		else
+			set_chr( TREASURE_CH,563,    3,7,    -400, 0,  0,	7,   270, 0,";")			//①宝箱（並）
+	}
+//■宝箱配置────────────────────────────────────────────────────────────
+
+
+
+
 	//ゲーセン用
 	if(GW_ENTRY_EVENT==101)//地蟲アークシェロブ戦帰り
 	{
@@ -415,6 +486,46 @@ INIT
 		EV("EV_BOSS_GAME_13_02B")
 	}
 
+
+
+}
+
+
+//■宝箱出現イベント────────────────────────────────────────────────────────────
+//ゲーセンコンプリートご褒美
+EV_SPAWN_TREASUREBOX
+{
+	if(!F1_04_GameCenCmp)
+	{
+			
+		if(WK001==2)
+		{
+			F_set(F1_04_GameCenCmp)			//★ゲーセンコンプリート／宝箱出現
+			
+			color(TREASURE_CH,-1)
+				
+			cross_fade(30)
+			CAM_move_chr(TREASURE_CH,0,0)
+			wait_CAM_move()
+			wait_fade()
+			wait(20)
+			
+			SE( 1016, TREASURE_CH)
+
+			EFF_chr(24580, TREASURE_CH, 0, 100, -1, "root")
+			
+			color(TREASURE_CH,20)
+			wait(60)		
+			
+			fade_in(100,30,0)
+			wait_fade()
+			CAM_return(0)
+			CAM(670,112,80,23,180,0,0)
+			wait(15)
+			fade_in(0,30,0)
+			wait_fade()	
+		}	
+	}
 }
 
 
@@ -432,6 +543,10 @@ EV_BOSS_GAME_01B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+			
 	TK_end()
 }
 //水魔エフェメルガ
@@ -446,6 +561,10 @@ EV_BOSS_GAME_02B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //妖花アビスフラワー
@@ -460,6 +579,10 @@ EV_BOSS_GAME_03B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //火竜ファブニール
@@ -474,6 +597,10 @@ EV_BOSS_GAME_04B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //大岩龍ガルガリオン
@@ -488,6 +615,10 @@ EV_BOSS_GAME_05B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //猫魔人モンブラン
@@ -502,6 +633,10 @@ EV_BOSS_GAME_06B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //人狼戦士ダイガルド
@@ -516,6 +651,10 @@ EV_BOSS_GAME_07B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+		
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //魔剣使いテルミドール
@@ -530,6 +669,10 @@ EV_BOSS_GAME_08B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //ダークアルウェン
@@ -541,10 +684,13 @@ EV_BOSS_GAME_09B
 	chr_pos(RAGNA,		6300,11150,0,210,	2)
 	chr_pos(PARTNER, 	6500,11150,0,120,	2)
 	chr_pos(PET,	 	6400,11300,0,180,	2)
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //月の戦鬼ダイガルド
@@ -559,6 +705,10 @@ EV_BOSS_GAME_10B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //吸血侯爵ザハール
@@ -573,6 +723,10 @@ EV_BOSS_GAME_11_01B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+	
 	TK_end()
 }
 //真祖ザハール
@@ -587,6 +741,10 @@ EV_BOSS_GAME_11_02B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //聖討将軍テルミドール
@@ -601,6 +759,10 @@ EV_BOSS_GAME_12B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //メルセデク．コア
@@ -615,6 +777,10 @@ EV_BOSS_GAME_13_01B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 //魔王ルシアン
@@ -629,6 +795,10 @@ EV_BOSS_GAME_13_02B
 	EV("SET_WARP_FLAG")
 	wait_EV("SET_WARP_FLAG")
 	wait_fade()
+	
+	EV("EV_SPAWN_TREASUREBOX")
+	wait_EV("EV_SPAWN_TREASUREBOX")
+		
 	TK_end()
 }
 
@@ -639,6 +809,14 @@ EV_BOSS_GAME_13_02B
 //使わないタイミングもあるけど一括入力。
 SET_WARP_FLAG
 {
+	//0924追加
+	if(!F6_00_GoToMeru)
+	{
+		SCORE(-2,92,0);//異世界．中継１	ダークアルウェン
+		SCORE(-2,93,0);//異世界．中継２	真ダイガルド
+		SCORE(-2,94,0);//異世界．終点	ザハール／真ザハール
+	}
+
 	//▼□
 	if(F6_00_GoToMeru)
 		workG(GW_WARP_FLAG,SET,1)//ワープ許可
diff --git a/scp_jp_conv/map/0/EV00533.txt b/scp_conv/map/0/EV00533.txt
index 66874fe..1fbce5c 100644
--- a/scp_jp_conv/map/0/EV00533.txt
+++ b/scp_conv/map/0/EV00533.txt
@@ -130,7 +130,7 @@ INIT
 		set_chr(19, 365,  5,6,	2800,-300,	140,	-115,0,0,";");
 	if(F2827)
 		set_chr(20, 366,  5,6,	3200,-300,	140,	-150,0,0,";");
-	if(F2811)
+	if(F2711)
 		set_chr(21, 126,  5,6,	3600,-300,	140,	-100,0,0,";");
 	if(F2817)
 		set_chr(22, 353,  5,6,	4000,-300,	140,	-100,0,0,";");
@@ -275,7 +275,7 @@ INIT
 		workL(001,ADD,1)
 	if(F2827)
 		workL(001,ADD,1)
-	if(F2811)
+	if(F2711)
 		workL(001,ADD,1)
 	if(F2817)
 		workL(001,ADD,1)
diff --git a/scp_jp_conv/map/0/EV00535.txt b/scp_conv/map/0/EV00535.txt
index 5949d61..b93313e 100644
--- a/scp_jp_conv/map/0/EV00535.txt
+++ b/scp_conv/map/0/EV00535.txt
@@ -121,7 +121,7 @@ INIT
 		set_chr(17, 136,  3,6,	4100,-300,	140,	-100,0,0,";");
 	if(F2773)
 		set_chr(18, 229,  3,6,	4375,-300,	140,	-100,0,0,";");
-	if(F2790)
+	if(F2791)
 		set_chr(19, 269,  3,6,	4650,-300,	140,	-100,0,0,";");
 	if(F2796)
 		set_chr(20, 277,  3,6,	4925,-300,	140,	-100,0,0,";");
@@ -223,7 +223,7 @@ INIT
 		workL(001,ADD,1)
 	if(F2773)
 		workL(001,ADD,1)
-	if(F2790)
+	if(F2791)
 		workL(001,ADD,1)
 	if(F2796)
 		workL(001,ADD,1)
diff --git a/scp_jp_conv/map/0/EV00536.txt b/scp_conv/map/0/EV00536.txt
index f8edd8d..57ca197 100644
--- a/scp_jp_conv/map/0/EV00536.txt
+++ b/scp_conv/map/0/EV00536.txt
@@ -101,9 +101,9 @@ INIT
 		set_chr(7, 	231,  3,6,	1600,-300,	140,	-100,0,0,";");
 	if(F2757)                  
 		set_chr(8, 	213,  3,6,	1900,-300,	140,	-100,0,0,";");
-	if(F2721)                  
-		set_chr(9, 	282,  3,6,	2200,-300,	140,	-100,0,0,";");
 	if(F2833)                  
+		set_chr(9, 	282,  3,6,	2200,-300,	140,	-100,0,0,";");
+	if(F2830)                  
 		set_chr(10,	372,  3,6,	2500,-300,	140,	-100,0,0,";");
 
 	if(F2716)
@@ -117,9 +117,9 @@ INIT
 	if(F2800)
 		set_chr(15, 281,  3,6,	6200,-300,	140,	-100,0,0,";");
 
-	if(F2701)
+	if(F2831)
 		set_chr(16, 370,  5,6,	3100,-300,	140,	-100,0,0,";");
-	if(F2701)
+	if(F2832)
 		set_chr(17, 371,  5,6,	3700,-300,	140,	-100,0,0,";");
 
 
@@ -139,6 +139,7 @@ INIT
 	F_set_chr(14,CF_NO_MINIMAP)
 	F_set_chr(15,CF_NO_MINIMAP)
 	F_set_chr(16,CF_NO_MINIMAP)
+	F_set_chr(17,CF_NO_MINIMAP)
 	
 //フィギュア台────────────────────────────────────────────────────────────
 
@@ -199,10 +200,10 @@ INIT
 		workL(001,ADD,1)
 	if(F2757)                  
 		workL(001,ADD,1)
-	if(F2721)                  
-		workL(001,ADD,1)
 	if(F2833)                  
 		workL(001,ADD,1)
+	if(F2830)                  
+		workL(001,ADD,1)
 
 	if(F2716)
 		workL(001,ADD,1)
@@ -215,9 +216,9 @@ INIT
 	if(F2800)
 		workL(001,ADD,1)
 
-	if(F2701)
+	if(F2831)
 		workL(001,ADD,1)
-	if(F2701)
+	if(F2832)
 		workL(001,ADD,1)
 	if(F2837)
 		workL(001,ADD,1)
diff --git a/scp_jp_conv/map/0/EV00600.txt b/scp_conv/map/0/EV00600.txt
index d6de88e..b9653be 100644
--- a/scp_jp_conv/map/0/EV00600.txt
+++ b/scp_conv/map/0/EV00600.txt
@@ -68,6 +68,9 @@ INIT
 
 	set_chr(100,990,	-1,-1,     0,-5300,  200,    0, 0813, 6,"<EV_SeeFirst>")	//初見イベント用
 
+	//アタリ
+	set_chr( 81,991,	-1,-1,	 -1520,3830,-1450,   0,  0202,	0,";")		//0922追加
+
 	//NPC
 	
 
@@ -619,7 +622,11 @@ EV_Meets_Cleese
 	look_off(RAGNA)
 	look_off(PET)
 	look_off(PARTNER)
-
+	
+	KAO(RAGNA,   "1","1","1")
+	KAO(PARTNER, "9","1","7")
+	KAO(PET,     "1","1","1")
+	
 	//カメラを初期設定に
 	CAM_return( 0 )
 	wait(30)
@@ -885,15 +892,15 @@ EV_Survant_Cleese
 	fade_in(100,30,BLACK)
 	wait_fade()
 
+	KAO(RAGNA,   "1","1","1")
+	KAO(PARTNER, "9","1","7")
+	KAO(PET,     "1","1","1")
+
 	//カメラを初期設定に
 	CAM_return( 0 )
 	wait(30)
 
 	F_reset_chr(CLEESE,CF_NO_CSP)
-
-	KAO(RAGNA,"1","1","1")
-	KAO(PET,"1","1","1")
-	KAO(PARTNER,"1","1","1")
 	
 	F_set_chr(S_MONTBLANC,CF_NO_MOVE)
 	F_set_chr(CLEESE,CF_NO_MOVE)
diff --git a/scp_jp_conv/map/0/EV00601.txt b/scp_conv/map/0/EV00601.txt
index 9d05543..f2d729d 100644
--- a/scp_jp_conv/map/0/EV00601.txt
+++ b/scp_conv/map/0/EV00601.txt
@@ -450,7 +450,7 @@ EV_5_22_ReturnCrystal
 	F_set_chr(LUE,CF_NO_CSP)
 
 	wait(1)
-	chr_equip( ALWEN,"wp_004", "Bone_RightSword", 100)	//杖を装備させるのはこちら。
+	chr_equip( ALWEN,"wp_004b", "Bone_RightSword", 100)	//杖を装備させるのはこちら。
 //	MOT(AWEN,53,1)										//アルウェンの右手を開かせる。
 
 	//カメラ初期位置
diff --git a/scp_jp_conv/map/0/EV00602.txt b/scp_conv/map/0/EV00602.txt
index 6b875ce..6ef4c03 100644
--- a/scp_jp_conv/map/0/EV00602.txt
+++ b/scp_conv/map/0/EV00602.txt
@@ -82,12 +82,12 @@ EV_LocateZacos
 
 
 	set_chr(MONSTER_D1,	  144,-1,-1,   -200,10000,4680,		 2,   0, 0, "D0_36;")	// くまこぶたー
-		set_chr( 36,		  808,-1,-1,      0, 8000,5480,		 3,   0, 0, "")	// トゲ球
+		set_chr( 36,		  808,-1,-1,      0, 8000,5480,		 4,   0, 0, "")	// トゲ球
 		chr_equip_chr(36,MONSTER_D1,"Bone_Hips", 125,  0, 0,0,	 0,50,25);
 
 
 	set_chr(MONSTER_D2,	  144,-1,-1,    200, 9000,5080,		 2,   0, 0, "D0_37;")	// くまこぶたー
-		set_chr( 37,		  808,-1,-1,      0, 8000,5480,		 3,   0, 0, "")	// トゲ球
+		set_chr( 37,		  808,-1,-1,      0, 8000,5480,		 4,   0, 0, "")	// トゲ球
 		chr_equip_chr(37,MONSTER_D2,"Bone_Hips", 125,  0, 0,0,	 0,50,25);
 
 
diff --git a/scp_jp_conv/map/0/EV00800.txt b/scp_conv/map/0/EV00800.txt
index ba51247..aa245c3 100644
--- a/scp_jp_conv/map/0/EV00800.txt
+++ b/scp_conv/map/0/EV00800.txt
@@ -2039,7 +2039,7 @@ EV_6_17_GameClear_to2
 		get_item(201,1,1)
 	}
 	else
-	if(GW_TREASURE<47)
+	if(GW_TREASURE<48)				//パッチ 2008/09/22 47 -> 48 変更
 	{
 		get_item(162,1,1)
 		get_item(166,1,1)
@@ -2155,6 +2155,9 @@ EV_6_17_GameClear_to2
 	menuTXT(3,	"■セーブしない",	20,GREEN)
 	menuEVENT(3,"EV_SAVE_OFF","EV_SAVE_OFF","")
 
+//	name("システムメッセージ")
+	MES_pos(0,"C3このクリアデータをロードすることにより、\n一部のデータを引き継いだ状態で、\n物語の始めからプレーする事ができます。\nまた各種追加要素も遊べるようになります。",2,172,296,300,100)
+
 	wait_W(WK_YESNO)
 
 	menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
@@ -2162,6 +2165,8 @@ EV_6_17_GameClear_to2
 	menu(3,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
 	wait_menu(1)
 
+	MES_close(0)
+
 	if(WK_YESNO==2)
 	{
 	}
diff --git a/scp_jp_conv/map/0/EV10902.txt b/scp_conv/map/0/EV10902.txt
index 772e482..68f3513 100644
--- a/scp_jp_conv/map/0/EV10902.txt
+++ b/scp_conv/map/0/EV10902.txt
@@ -81,6 +81,10 @@ INIT
 	//set_chr( 1,622,	1,4,    0800, 0500,  0,    2, 0,	0,"") //石像（髑髏）
 	set_chr( 1,623,	1,4,    1200, 0500,  0,    2, 0,	0,"") //ガスコンロ
 	set_chr( 1,624,	1,4,    1600, 0500,  0,    2, 0,	0,"") //回転刃
+	//set_chr( 1,760,	1,4,    0000, 1000,  0,    2, 0,	0,"") //ボスゲーム筐体1
+	set_chr( 1,773,	1,4,    0000, 1000,  0,    2, 0,	0,"") //ボスクラウン1
+	//set_chr( 1,765,	1,4,    0400, 1000,  0,    2, 0,	0,"") //ボスゲーム筐体2
+	set_chr( 1,774,	1,4,    0400, 1000,  0,    2, 0,	0,"") //ボスクラウン2
 
 	set_chr( 1,633,	3,1,   -600,0,  0,      2,  270,	0,"") //ヒビ壁
 	set_chr( 1,633,	3,1,   -1000,0,  0,      2,  90,	0,"") //ヒビ壁
diff --git a/scp_jp_conv/map/0/EV20901.txt b/scp_conv/map/0/EV20901.txt
index da7571e..eb7e7ab 100644
--- a/scp_jp_conv/map/0/EV20901.txt
+++ b/scp_conv/map/0/EV20901.txt
@@ -99,6 +99,10 @@ INIT
 	set_chr( 60,097,	3,4,   0700,1000,  0,  	 2,  0,	20,"") //カイ忍者服
 	set_chr( 61,062,	3,4,   1200,1000,  0,  	 2,  0,	20,"") //カイ包帯
 
+	set_chr( 61,081,	3,4,   -300,1500,  0,  	 2,  0,	20,"") //ペンギン
+	set_chr( 61,1006,	3,4,   -100,1500,  0,  	 2,  0,	20,"") //ペンギン仲間用
+	set_chr( 61,1106,	3,4,   0200,1500,  0,  	 2,  0,	20,"") //イワトビペンギン
+
 
 }
 
diff --git a/scp_jp_conv/map/0/EV52902.txt b/scp_conv/map/0/EV52902.txt
index 5c28095..d1ad5d9 100644
--- a/scp_jp_conv/map/0/EV52902.txt
+++ b/scp_conv/map/0/EV52902.txt
@@ -69,9 +69,7 @@ INIT
 	set_chr( 1,99,1,4,     2000,1000,  0,  	 2,  0,	0,"") //女子高制服アルウェン
 
 	set_chr( 1,1064,1,4,   -400,1500,  0,  	 2,  0,	0,"") //セピアテルミドール
-
-
-
+	set_chr( 1,1069,1,4,    000,1500,  0,  	 2,  0,	0,"") //パンクロック
 }
 
 #EndScriptTable
diff --git a/scp_jp_conv/map/0/MC00012.bmp b/scp_conv/map/0/MC00012.bmp
index 9faba38..7215eff 100644
Binary files a/scp_jp_conv/map/0/MC00012.bmp and b/scp_conv/map/0/MC00012.bmp differ
diff --git a/scp_jp_conv/map/0/MC00042.bmp b/scp_conv/map/0/MC00042.bmp
index ac7a942..558f2ee 100644
Binary files a/scp_jp_conv/map/0/MC00042.bmp and b/scp_conv/map/0/MC00042.bmp differ
diff --git a/scp_jp_conv/map/0/MC00052.bmp b/scp_conv/map/0/MC00052.bmp
index ac7a942..94b9bba 100644
Binary files a/scp_jp_conv/map/0/MC00052.bmp and b/scp_conv/map/0/MC00052.bmp differ
