diff --git a/scp_jp_conv/map/6/EV21751.txt b/scp_conv/map/6/EV21751.txt
index 5dde639..39bec87 100644
--- a/scp_jp_conv/map/6/EV21751.txt
+++ b/scp_conv/map/6/EV21751.txt
@@ -12,6 +12,8 @@
 
 //■ローカルフラグ
 
+#BOSS_CH		1
+
 #TREASURE_CH	49
 #Fx_TREASURE	2312	//☆012アンバー
 
@@ -57,25 +59,6 @@ INIT
 	set_chr( 96,804,	 8, 6,  -350,-350,115,		  0,   270, 8,"(L2?99 [9991ホシフリンデ] WT?30 L2!99 [9903] WT?30);")	//①看板
 
 
-//■敵
-	set_chr(  1,281,	 4, 7,   900,-200,  0,		  6,     0, 0,"SF111 <EV_BossFinish>;")	//①敵 
-	EV("EV_BossDeactivate")
-
-//■宝箱
-	if( !Fx_TREASURE )
-	{
-		set_chr( TREASURE_CH,561,	4, 7,   900,-300,  0,     6,     0,20,"<TK_TREASURE>;")
-		set_chr(150,990, 	0, 0,     0,   0,  0,     0,     0, 8,"#3_49 F1 WT?10 <EV_BossBoxFall> WT?25 #2_49;")
-	}
-	else
-	{
-		set_chr( TREASURE_CH,561,	4, 7,   900,-300,  0,     7,     0, 0,";")
-		set_chr(150,990,	0, 0,     0,   0,  0,	  0,     0, 8,"#3_49 F1 WT?10 <EV_BossBoxFall> WT?25;")
-	}
-	chr_equip_chr( 49, 1,"Bone_Hips", 100,  90,0,0,		0, 0, 0);	//背負う箱
-	color( 49,-1)		// 透明に
-	F_set_chr( 49,		CF_NO_MINIMAP)	// 宝箱 ミニマップ非表示
-
 //■
 //  -------  no typ   	  tip      x    y   z       mot     向 状  000+++++++010+++++++020+++++++030+++++++040+++++++050+++++++060+++++++070+++++++080+++++++090+++++++100+++++++110+++++++120+++++++130+++++++140+++++++150+++++++160+++++++170+++++++180+++++++190+++++++200+++++++210+++++++220+++++++230+++++++240+++++++250++
 	set_chr(112,627,	 7, 6,     0,-400,  0,		  0,   180, 0,";")	//柵小
@@ -191,10 +174,50 @@ EV_BossActivate
 {
 	if ( !F1 )
 	{
+	//■敵
 		F_set(109)		// 警報指示
+		wait(120)
+
+		workL(001,RAND,4)
+		if(WK001==0)
+			set_chr( 1,281,	 4, 7,   900,-300,  0,     6,     0, 0,"SF111 <EV_BossFinish>;")	//①敵 
+		else if(WK001==1)
+			set_chr( 1,281,	 4, 6,   900, 300,  0,     6,     0, 0,"SF111 <EV_BossFinish>;")	//①敵 
+		else if(WK001==2)
+			set_chr( 1,281,	 4, 6,   300, 900,  0,     6,     0, 0,"SF111 <EV_BossFinish>;")	//①敵 
+		else
+			set_chr( 1,281,	 5, 6,  -300, 900,  0,     6,     0, 0,"SF111 <EV_BossFinish>;")	//①敵 
+
+//		set_chr(  1,281,	 4, 7,   900,-200,  0,		  6,     0, 0,"SF111 <EV_BossFinish>;")	//①敵 
+		MOT( 1, 6, 0)		// イベント用待機
+		F_set_chr(  1,		CF_NO_MINIMAP)	// ボス ミニマップ非表示
+		F_set_chr(  1,		CF_NO_CLIP2)
+		F_set_chr(  1,		CF_NO_HPBAR)	// ボス HPバー非表示
+		F_set_chr(  1,		CF_NO_CSP)		// ボス 当たりなし
+		color(  1,-1)		// 透明に
+
+//		EV("EV_BossDeactivate")
+//		wait_EV("EV_BossDeactivate")
+		F_set(105)	// EV_BossDeactivateよりあと
+
+	//■宝箱
+		if( !Fx_TREASURE )
+		{
+			set_chr( TREASURE_CH,561,	4, 7,   900,-300,  0,     6,     0,20,"<TK_TREASUREX>;")
+			set_chr(150,990, 	0, 0,     0,   0,  0,     0,     0, 8,"#3_49 F1 WT?10 <EV_BossBoxFall> WT?25 #2_49;")
+		}
+		else
+		{
+			set_chr( TREASURE_CH,561,	4, 7,   900,-300,  0,     7,     0, 0,";")
+			set_chr(150,990,	0, 0,     0,   0,  0,	  0,     0, 8,"#3_49 F1 WT?10 <EV_BossBoxFall> WT?25;")
+		}
+		chr_equip_chr( 49, 1,"Bone_Hips", 100,  90,0,0,		0, 0, 0);	//背負う箱
+		color( 49,-1)		// 透明に
+		F_set_chr( 49,		CF_NO_MINIMAP)	// 宝箱 ミニマップ非表示
+
+		wait( 30)
 
 		MOT( 1, 34, 0)		// ワープ
-		wait(120)
 
 		color( 1,30)		// 不透明に
 		F_reset_chr(  1,	CF_NO_HPBAR)	// ボス HPバー表示
@@ -202,6 +225,7 @@ EV_BossActivate
 
 		F_set(108)
 
+		SE(1050, 0)
 		EFF_chr( 8100, 1,	0,	50,	0,"Bone_Hips")
 	}
 }
@@ -220,6 +244,7 @@ EV_BossDeactivate
 
 		if( F105 )
 		{
+			delete( 1 );	// BOSS_CH
 			wait( 30 )
 			F_reset(105)
 			wait( 60 )
@@ -314,7 +339,6 @@ EV_BossManage2
 			{
 				if ( F110 )
 				{
-					F_set(105)
 					EV("EV_BossActivate")
 				}
 			}
@@ -386,6 +410,27 @@ EV_EnterFirst
 	EV("EV_BossManage2")
 }
 
+//--------------------------------------------------------------------
+//トレジャー発見
+TK_TREASUREX
+{
+	TK_begin()
+	rot_chr(0,60,TREASURE_CH)
+
+	MOT(TREASURE_CH,1,0)
+	wait(30)
+	fade_in(30,10,BLACK)
+	F_set(Fx_TREASURE)//2300～2400
+	get_item(140,1,0)//謎の小箱　鑑定前
+	wait(10)
+	wait_key(0)
+	fade_in(0,10,BLACK)
+	menu(1,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+	menu(0,		-1,	-1,-1,-1,	-1,-1,	10,0,0)
+
+	TK_end()
+}
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/6/EV60001.txt b/scp_conv/map/6/EV60001.txt
index f538783..82616e3 100644
--- a/scp_jp_conv/map/6/EV60001.txt
+++ b/scp_conv/map/6/EV60001.txt
@@ -50,6 +50,8 @@
 // 01 リトライ用コース
 // 02 クリア済み判定用
 // 05 カッパリトライ処理を飛ばす。
+// 06 リトライ用ワーク
+// 07 リトライ用ワーク
 // 10 カッパ一般会話用のランダムナンバー
 //
 //ローカルフラグ
@@ -150,6 +152,12 @@ INIT
 		else if(GW_ENTRY_EVENT==13)
 			workL(00,SET,13)
 
+		if(GW_ENTRY_EVENT>4)	//クリアできなかった
+		{
+			if(GW_SKI_MISS<5)
+				workG(GW_SKI_MISS,ADD,1)	//ミスを加算
+		}
+
 		//今クリアしてきたコース番号
 		if(GW_SKI_MODE==1)
 			workL(01,SET,1)
@@ -874,7 +882,7 @@ EV_2_18_PipiroPockle
 //	set_chr(EVENT_RAGNA,   1010,-1,-1, -376,2265,-221,2,190,0, "")
 	set_chr(ALWEN,         1011,-1,-1, -661,2685,-284,2,190,0, "")
 //	set_chr(ALWEN,         1011,-1,-1, -551,2216,-216,2,190,0, "")
-	chr_equip( ALWEN,"wp_004b", "Bone_RightSword", 100)	//杖を装備させるのはこちら。
+	chr_equip( ALWEN,"wp_004", "Bone_RightSword", 100)	//杖を装備させるのはこちら。
 //	MOT(ALWEN,53,1)										//アルウェンの右手を開かせる。
 
 	F_set_chr(PIPIRO, CF_NO_CLIP)
@@ -994,7 +1002,7 @@ EV_2_18_PipiroPockle
 	rot(PIPIRO, 30, 40)
 	rot(POCKLE, 30, 40)
 	wait_fade()
-	wait_move(EVENT_RANGA)
+	wait_move(EVENT_RAGNA)
 	wait_move(ALWEN)
 
 	KAO(POCKLE,"12321Z3", "1233321", "6")
@@ -1022,7 +1030,7 @@ EV_2_18_PipiroPockle
 	
 	look_chr(EVENT_RAGNA, ALWEN, "Bone_Head")
 	
-	EMO(EVENT_RANGA, EMO_HATENA)
+	EMO(EVENT_RAGNA, EMO_HATENA)
 	KAO(EVENT_RAGNA, "B", "321D", "6")
 	wait(30)
 	KAO(EVENT_RAGNA, "2", "D", "6")	
diff --git a/scp_jp_conv/map/6/EV60101.txt b/scp_conv/map/6/EV60101.txt
index 3540982..a0db0a9 100644
--- a/scp_jp_conv/map/6/EV60101.txt
+++ b/scp_conv/map/6/EV60101.txt
@@ -30,7 +30,7 @@ INIT
 	set_chr( 52,654,	 5, 5,  -225,-350,  0,		  2,     0, 0,";")				//①順路案内（メイン）
 
 
-	if( F4_05_OnVillage2 && !F4_17_InTheEvening			//里についてから夕方まで配置
+	if( F4_05_OnVillage2 && !F4_17_InTheEvening )			//里についてから夕方まで配置
 	{
 		set_chr( DAIGORO	,74,-1,-1,  9070,10859,1,	2,270, 20,"<TK_DAIGORO2>")		//ダイゴロー セーブポイント付近
 		F_set_chr(DAIGORO,CF_NO_MOVE)
diff --git a/scp_jp_conv/map/6/EV60111.txt b/scp_conv/map/6/EV60111.txt
index a533d0e..3d1c011 100644
--- a/scp_jp_conv/map/6/EV60111.txt
+++ b/scp_conv/map/6/EV60111.txt
@@ -51,6 +51,9 @@
 
 // 2185 メイン③ □岩
 
+// 2190 メイン③ ⑧大砲
+// 2191 メイン③ □大砲
+
 //■ローカルフラグ
 
 //--------------------------------------------------------------------
diff --git a/scp_jp_conv/map/6/EV60121.txt b/scp_conv/map/6/EV60121.txt
index d84a81f..7348ff9 100644
--- a/scp_jp_conv/map/6/EV60121.txt
+++ b/scp_conv/map/6/EV60121.txt
@@ -54,7 +54,7 @@ INIT
 	{
 	// 初回
 		set_chr( 61,570,	 2, 4,    50,   0,  0,		  6,   270, 5,"M6?99 M5_99 SF2103;")	//②ボタンスイッチ
-		set_chr(150,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2103 O1_18 WT?10 C0_72 WT?20 V4_72 #8_72  WT?30 C0_73 V4_73 #8_73  V4_74 #8_74 WT?30 C0_0;") //
+		set_chr(150,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2103 O1_18 WT?10 C0_72 WT?20 V2_72 #8_72 O1_1318   WT?30 C0_73 V2_73 #8_73 O1_1318     V2_74 #8_74 O1_1318    WT?30 C0_0;") //
 	}
 	else
 	{
@@ -68,7 +68,7 @@ INIT
 	{
 	// 初回
 		set_chr( 62,570,	 3, 1,     0,  50,  0,		  6,     0, 5,"M6?99 M5_99 SF2104;")	//③ボタンスイッチ
-		set_chr(151,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2104 O1_18 WT?10 C0_75 WT?20 V4_75 #8_75 WT?30 C0_0;") //
+		set_chr(151,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2104 O1_18 WT?10 C0_75 WT?20 V2_75 #8_75 O1_1318   WT?30 C0_0;") //
 	}
 	else
 	{
@@ -183,10 +183,10 @@ INIT
 	set_chr( 70,669,	 5, 4,   600,-275,  0,		  3,    90, 0,";") //①扇風機a
 	set_chr( 71,669,	 5, 4,   600,  75,  0,		  3,    90, 0,";") //①扇風機b
 
-	set_chr( 72,677,	 3, 4,   500,-300,150,		 -1,     0, 8,"O0_1318 WT?30 X1_450 WT?20 ( X1_-900 WT?20 X1_900 WT?20 );")	//②移動床小（森）
-	set_chr( 73,677,	 4, 4,  -725,   0,150,		 -1,     0, 8,"O0_1318 WT?75 X1_450 WT?20 ( X1_-900 WT?20 X1_900 WT?20 );")	//③移動床小（森）
-	set_chr( 74,677,	 4, 4,   550,   0,150,		 -1,     0, 8,"O0_1318 WT?120 X1_-450 WT?20 ( X1_900 WT?20 X1_-900 WT?20 );")	//④移動床小（森）
-	set_chr( 75,677,	 5, 4,     0,-200,150,		 -1,     0, 8,"O0_1318 Y1_-225 WT?20 ( Y1_450 WT?10 Y1_-450 WT?10 );")	//⑤移動床小（森）
+	set_chr( 72,677,	 3, 4,   500,-300,150,		 -1,     0, 8,"WT?30 X1_450 WT?20 ( X1_-900 WT?20 X1_900 WT?20 );")	//②移動床小（森）
+	set_chr( 73,677,	 4, 4,  -725,   0,150,		 -1,     0, 8,"WT?75 X1_450 WT?20 ( X1_-900 WT?20 X1_900 WT?20 );")	//③移動床小（森）
+	set_chr( 74,677,	 4, 4,   550,   0,150,		 -1,     0, 8,"WT?120 X1_-450 WT?20 ( X1_900 WT?20 X1_-900 WT?20 );")	//④移動床小（森）
+	set_chr( 75,677,	 5, 4,     0,-200,150,		 -1,     0, 8,"Y1_-225 WT?20 ( Y1_450 WT?10 Y1_-450 WT?10 );")	//⑤移動床小（森）
 
 	set_chr( 76,660,	 7, 4,  -100,-900,450,		  4,     0, 0,";")	//⑥プロペラ移動床
 	set_chr( 77,660,	 6, 4,  -550,   0,450,		  4,     0, 0,";")	//⑦プロペラ移動床
diff --git a/scp_jp_conv/map/6/EV60131.txt b/scp_conv/map/6/EV60131.txt
index d95c0f9..1d15ab8 100644
--- a/scp_jp_conv/map/6/EV60131.txt
+++ b/scp_conv/map/6/EV60131.txt
@@ -128,12 +128,22 @@ INIT
 		color2(128, 41,81,100, 0,0,0)
 
 	set_chr(130,661,	 8, 9,  -600, -950, 0,		  2,   180, 8,"M3_99 (SF107 Y2_4300 RF107 M4_99 WT?15 SF107 Y2_-4300 RF107 M3_99 WT?15);"); //⑦リフト台[路線A]
-	set_chr(131,810,	 8, 9,  -600, -950,50,		  2,     0, 8,"(Y2_4300 WT?15 Y2_-4300 WT?15);"); //⑧大砲[路線A]
+	if ( !F2190 )
+	{
+		set_chr(131,810,	 8, 9,  -600, -950,50,		  2,     0, 8,"(Y2_4300 WT?15 Y2_-4300 WT?15);"); //⑧大砲[路線A]
+		set_chr(181,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F131 I_$$$2 SF2190;");
+		chr_equip_chr(181,131,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
+	}
 
 	set_chr(132,661,	 7, 8,   150,-1200, 0,		  2,   180, 8,"M3_99 (SF108 Y2_3750 RF108 M4_99 WT?15 SF108 Y2_-3750 RF108 M3_99 WT?15);"); //⑩リフト台[路線B]
 
 	set_chr(134,661,	 7, 6,  -150, -300, 0,		  2,   180, 8,"M3_99 (SF109 Y2_4550 RF109 M4_99 WT?15 SF109 Y2_-4550 RF109 M3_99 WT?15);"); //□リフト台[路線C]
-	set_chr(135,810,	 7, 6,  -150, -300,50,		  2,     0, 8,"(Y2_4550 WT?15 Y2_-4550 WT?15);"); //□大砲[路線C]
+	if ( !F2191 )
+	{
+		set_chr(135,810,	 7, 6,  -150, -300,50,		  2,     0, 8,"(Y2_4550 WT?15 Y2_-4550 WT?15);"); //□大砲[路線C]
+		set_chr(185,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F135 I_$$$2 SF2191;");
+		chr_equip_chr(185,135,"obx0574:Layer1(1)",  100, 0,0,0,	0,0,45);
+	}
 
 	if ( !F2185 )
 	{
diff --git a/scp_jp_conv/map/6/EV61221.txt b/scp_conv/map/6/EV61221.txt
index 6dd3528..d1797bb 100644
--- a/scp_jp_conv/map/6/EV61221.txt
+++ b/scp_conv/map/6/EV61221.txt
@@ -160,7 +160,7 @@ INIT
 //■宝箱
 
 	if ( !Fx_622Bomb1 )
-		set_chr( WOODBOX_CH,562,	1, 6,   365,-450,  0,		 2,    30,20,"<TK_WOODBOX_X> <EV_SetGetBomb1>;")	//①木箱
+		set_chr( WOODBOX_CH,562,	1, 6,   365,-450,  0,		 6,    30,20,"<TK_WOODBOX_X> <EV_SetGetBomb1>;")	//①木箱
 	else
 		set_chr( WOODBOX_CH,562,	1, 6,   365,-450,  0,		 7,    30, 0,";")	//①木箱
 
@@ -183,8 +183,7 @@ INIT
 
 	if ( !F2132 )
 	{
-		set_chr( 69 641,	 3, 4,  -400, 250,  0,		  5,     0, 0,"#0_78;")	//⑥パラボラアンテナ
-		set_chr(169,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F67 I_$$$2 SF2132;");
+		set_chr( 69 641,	 3, 4,  -400, 250,  0,		  5,     0, 0,"#0_78 I_$$$2 SF2132;")	//⑥パラボラアンテナ
 	}
 
 
diff --git a/scp_jp_conv/map/6/EV61231.txt b/scp_conv/map/6/EV61231.txt
index b281cdd..e463ac9 100644
--- a/scp_jp_conv/map/6/EV61231.txt
+++ b/scp_conv/map/6/EV61231.txt
@@ -261,16 +261,16 @@ INIT
 	if ( GW_LV_PLATE==0 )
 	{
 		if( !Fx_TREASURE )
-			set_chr( TREASURE_CH,561,	 4, 5,     0,   0,  0,  	 6,   0,20,"<TK_TREASURE>;")
+			set_chr( TREASURE_CH,561,	 4, 5,     0,   0,  0,  	 6, 270,20,"<TK_TREASURE>;")
 		else
-			set_chr( TREASURE_CH,561,	 4, 5,     0,   0,  0,  	 7,   0, 0,";")
+			set_chr( TREASURE_CH,561,	 4, 5,     0,   0,  0,  	 7, 270, 0,";")
 	}
 	else
 	{
 		if( !Fx_TREASURE2 )
-			set_chr( TREASURE2_CH,561,	 4, 5,     0,   0,  0,  	 6,   0,20,"<TK_TREASURE2>;")
+			set_chr( TREASURE2_CH,561,	 4, 5,     0,   0,  0,  	 6, 270,20,"<TK_TREASURE2>;")
 		else
-			set_chr( TREASURE2_CH,561,	 4, 5,     0,   0,  0,  	 7,   0, 0,";")
+			set_chr( TREASURE2_CH,561,	 4, 5,     0,   0,  0,  	 7, 270, 0,";")
 	}
 
 	if ( !Fx_623Food1 )
diff --git a/scp_jp_conv/map/6/EV62311.txt b/scp_conv/map/6/EV62311.txt
index 7b0a650..e6cfb8d 100644
--- a/scp_jp_conv/map/6/EV62311.txt
+++ b/scp_conv/map/6/EV62311.txt
@@ -182,19 +182,21 @@ INIT
 	set_chr(110,627,	 3, 3,     0,-900,  0,		  0,     0, 0,";")	// 柵小
 		color2(110, 41,81,100, 0,0,0)
 
-	set_chr( 70,643,	 5, 8,     0,   0,  1,		  6,     0, 0,";")	//①きのこ
-
-	set_chr( 69,643,	 7, 4,  -200,   0,  1,		  6,     0, 0,";")	//②きのこ
-		chr_equip2(69,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
-	set_chr( 68,643,	 8, 3,  -900,-200,  1,		  6,     0, 0,";")	//③きのこ
-		chr_equip2(68,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
-	set_chr( 67,643,	 8, 2,   200,-200,  1,		  6,     0, 0,";")	//④きのこ
-		chr_equip2(67,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
-	set_chr( 66,643,	 4, 4,     0,   0,  1,		  6,     0, 0,";")	//⑤きのこ
-		chr_equip2(66,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
-	set_chr( 65,643,	 4, 3,     0,-900,  1,		  6,     0, 0,";")	//⑥きのこ
-		chr_equip2(65,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
-
+	if ( !F2104 )
+	{
+		set_chr( 70,643,	 5, 8,     0,   0,  1,		  6,     0, 0,";")	//①きのこ
+
+		set_chr( 69,643,	 7, 4,  -200,   0,  1,		  6,     0, 0,";")	//②きのこ
+			chr_equip2(69,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
+		set_chr( 68,643,	 8, 3,  -900,-200,  1,		  6,     0, 0,";")	//③きのこ
+			chr_equip2(68,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
+		set_chr( 67,643,	 8, 2,   200,-200,  1,		  6,     0, 0,";")	//④きのこ
+			chr_equip2(67,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
+		set_chr( 66,643,	 4, 4,     0,   0,  1,		  6,     0, 0,";")	//⑤きのこ
+			chr_equip2(66,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
+		set_chr( 65,643,	 4, 3,     0,-900,  1,		  6,     0, 0,";")	//⑥きのこ
+			chr_equip2(65,	"eq_162",	"obx0194", 110,		-90,0,0,	0,0,380);	// 笠
+	}
 
 	if ( !F2120 )
 		set_chr( 73,630,	 5, 4,     0,-375,  0,		  2,    60, 0,"I_$$$1 SF2120;")	//⑦樽
@@ -228,6 +230,17 @@ INIT
 			set_chr(  2,373,	 5, 8,     0,   0,  0,		  2,     0, 0,"SF2106 V3_1 <EV_ActivateEvemy1>;")	// ①敵 当たり用ダミー
 				chr_equip2(2,	"eq_162",	"csp1",117,	-90,0,0,	0,0,-30);				// 笠 
 				chr_equip_chr( 2, 70, "obx0194", 100,	0,0,0,	0,0,350);	// 笠
+
+			// ①敵
+			F_set_chr( 1,CF_NO_MINIMAP)	// ミニマップ非表示
+			F_set_chr( 1,CF_NO_HPBAR)	// HPバー非表示
+			MOT( 1, 6, 0)		// イベント用待機
+
+			// 373ダミー
+			F_set_chr( 2,CF_NO_MINIMAP)	// ミニマップ非表示
+			F_set_chr( 2,CF_NO_HPBAR)	// HPバー非表示
+			F_set_chr( 2,CF_NO_SHADOW)	// 影描画なし
+			F_set_chr( 2,CF_NO_DROPITEM)  // ドロップアイテムを落とさない
 		}
 		else
 		{
@@ -246,16 +259,6 @@ INIT
 			chr_equip2(4,	"eq_164",	"csp1",117,	-90,0,0,	0,0,-30);				// 花笠青 
 			chr_equip_chr( 4, 5, "Bone_Kasa", 100,	0,0,0,	0,30,-60);	// 笠
 
-		// ①敵
-		F_set_chr( 1,CF_NO_MINIMAP)	// ミニマップ非表示
-		F_set_chr( 1,CF_NO_HPBAR)	// HPバー非表示
-		MOT( 1, 6, 0)		// イベント用待機
-
-		// 373ダミー
-		F_set_chr( 2,CF_NO_MINIMAP)	// ミニマップ非表示
-		F_set_chr( 2,CF_NO_HPBAR)	// HPバー非表示
-		F_set_chr( 2,CF_NO_SHADOW)	// 影描画なし
-		F_set_chr( 2,CF_NO_DROPITEM)  // ドロップアイテムを落とさない
 
 		// 374ダミー1
 		color(3, -1)	//非表示
@@ -278,19 +281,23 @@ INIT
 	{
 		set_chr(  1,132,	 5, 8,  -200,-200,  0,        0,   270, 0,";") //①敵 いちもくれん
 
-		set_chr(  3,374,	 5, 8,     0,   0,  0,		  2,     0, 0,";")		// きのこ 装着用ダミー
-			chr_equip2(3,	"eq_164",	"csp1",117,	-90,0,0,	0,0,-30);				// 花笠青 
-			chr_equip_chr( 3, 70, "obx0194", 100,	0,0,0,	0,0,350);	// 花笠青
+		if ( !F2104 )
+		{
+			set_chr(  3,374,	 5, 8,     0,   0,  0,		  2,     0, 0,";")		// きのこ 装着用ダミー
+				chr_equip2(3,	"eq_164",	"csp1",117,	-90,0,0,	0,0,-30);				// 花笠青 
+				chr_equip_chr( 3, 70, "obx0194", 100,	0,0,0,	0,0,350);	// 花笠青
+
+			// 374ダミー1
+			F_set_chr( 3,CF_NO_CSP)	//
+			F_set_chr( 3,CF_NO_MINIMAP)	// ミニマップ非表示
+			F_set_chr( 3,CF_NO_HPBAR)	// HPバー非表示
+			F_set_chr( 3,CF_NO_SHADOW)	// 影描画なし
+			F_set_chr( 3,CF_NO_DROPITEM)  // ドロップアイテムを落とさない
+		}
 
 		set_chr(  5,132,	 9, 5,     0, 600,  0,		  2,     0, 0,";") //②敵 いちもくれん
 			chr_state_LV(5, 1);
 
-		// 374ダミー1
-		F_set_chr( 3,CF_NO_CSP)	//
-		F_set_chr( 3,CF_NO_MINIMAP)	// ミニマップ非表示
-		F_set_chr( 3,CF_NO_HPBAR)	// HPバー非表示
-		F_set_chr( 3,CF_NO_SHADOW)	// 影描画なし
-		F_set_chr( 3,CF_NO_DROPITEM)  // ドロップアイテムを落とさない
 	}
 
 	set_chr(  7,132,	 6, 5,     0, 900,  0,		  2,   180, 0,";") //③敵 いちもくれん
@@ -317,7 +324,11 @@ INIT
 	set_chr( 80,990,	 4, 4,     0,   0,  0,		  0,071111, 6,"SF100;")	//⑨敵エリア
 	set_chr( 81,990,	 4, 3,  -200,-900,  0,		  0,070804, 6,"SF101;")	//□敵□敵エリア
 	set_chr( 82,990,	 5, 6,  -200,-200,  0,		  0,070808, 6,"SF102;")	//②敵エリア
-	set_chr( 83,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2106 L1?0470 C0_70 <EV_GiveHanagasa> WT?30 C0_0;")	//②敵エリア
+
+	if ( !FR_631_Delivered )
+	{
+		set_chr( 83,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"F2106 L1?0470 C0_70 <EV_GiveHanagasa> WT?30 C0_0;")	//②敵エリア
+	}
 
 	// 雪球距離
 	set_chr(180,990,	 0, 0,   0, 0, 0,   0,		  0,     9,"RF110 Ly?7700 SF110")
diff --git a/scp_jp_conv/map/6/EV62321.txt b/scp_conv/map/6/EV62321.txt
index 7a1c55d..4f112c0 100644
--- a/scp_jp_conv/map/6/EV62321.txt
+++ b/scp_conv/map/6/EV62321.txt
@@ -12,6 +12,7 @@
 #FR_631_GoenInit		2102
 
 //■ローカルフラグ
+// 103 中ボスBGM管理
 // 104 □敵を攻撃した
 // 105 関所で1000ペンネを支払った
 // 106 ⑥レバースイッチを押した
@@ -337,6 +338,16 @@ INIT
 				set_chr(150,990, 0, 0,     0,   0,  0,		  0,     0, 8,"#3_49 F1 WT?10 O1_18 SF2100 <EV_Enemy1BoxFall> WT?25       C0_61 WT?30 M4_61 WT?30 C0_0;")
 		}
 
+		// 中ボスBGM
+		set_chr(160,990,	 0, 0,     0,   0,  0,		  0,     0, 8,"(F103 <EV_BossBGM> WT?90 !F101 !F103 <EV_NormalBGM> WT?90);");
+// 岩を壊したらボスBGM
+		set_chr(161,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"!F2100 F109 SF103");	// ボスが生きていて、ボス戦闘中ならば103をセット
+
+// 警報がなったらボスBGM
+//		set_chr(161,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"!F2100 F110 SF103");	// ボスが生きていて、ボス戦闘中ならば106をセット
+//		set_chr(162,990,	 4, 2,     0,   0,  0,		  0,072323, 6,"!F2100 SF103");		// ボスが生きていて、ボス部屋内ならば106をセット
+
+		set_chr(163,990,	 0, 0,     0,   0,  0,		  0,     0, 9,"RF103");				// 103をクリア
 	}
 
 	set_chr(151,990,	 2, 3,     0,-450,  0,		  0,071002, 6,"#8_99 WT?2 SF112 M5_60 <EV_Enemy2Activate> WT?2 V2_2 F2 WT?10 O1_18 WT?20 C0_61 WT?30 M4_61 M4_60 WT?30 C0_0;")		// はにわおこじょ
@@ -380,12 +391,12 @@ INIT
 		chr_equip_chr( 27, 37,"TG1", 100,	0,0,180,	0,0,0);
 
 	set_chr(  8,128,	 8, 4,  -600,   0,  0,		  2,   180, 0,"D1_9;") //⑦敵a ちゃりおっと	標準Lv12 + 追加Lv4 = 16
-	set_chr(  9,810,	 8, 4,  -600,   0,  0,		  2,   180, 0,";") //④敵b 大砲
+	set_chr(  9,810,	 8, 4,  -600,   0,  0,		  2,   180, 0,"I_$$$2;") //④敵b 大砲
 		chr_equip_chr( 9, 8,"Null_Mon", 100,	0,  0,180,	0,0, 0);
 		chr_state_LV( 8, 7);
 
 	set_chr( 10,128,	 8, 4,     0,   0,  0,		  2,   180, 0,"D1_11;") //④敵a ちゃりおっと	標準Lv12 + 追加Lv4 = 16
-	set_chr( 11,810,	 8, 4,     0,   0,  0,		  2,   180, 0,";") //④敵b 大砲
+	set_chr( 11,810,	 8, 4,     0,   0,  0,		  2,   180, 0,"I_$$$2;") //④敵b 大砲
 		chr_equip_chr(11,10,"Null_Mon", 100,	0,  0,180,	0,0, 0);
 		chr_state_LV(11, 7);
 
@@ -708,6 +719,22 @@ TK_TREASUREX2
 	TK_end()
 }
 
+//--------------------------------------------------------------------
+EV_BossBGM
+{
+	stop_BGM(30)
+	wait(30)
+	BGM(35)
+}
+
+//--------------------------------------------------------------------
+EV_NormalBGM
+{
+	stop_BGM(30)
+	wait(30)
+	BGM(31)
+}
+
 #EndScriptTable
 //====================================================================
 
diff --git a/scp_jp_conv/map/6/EV62331.txt b/scp_conv/map/6/EV62331.txt
index 228a52a..8fe2bc7 100644
--- a/scp_jp_conv/map/6/EV62331.txt
+++ b/scp_conv/map/6/EV62331.txt
@@ -593,13 +593,13 @@ EV_ZizouFailed
 	CAM_move( 7650,-4100,160, 0,0);
 	wait(60)
 
-	MES(MINIKINO,"ごめんね。\nわたしだけ先に……。",0)
+	MES(MINIKINO,"ごめんね。\nわたしだけ先に……",0)
 	MES_close(MINIKINO)
 
-	MES(MINIKINO,"その扉はわたしの力では開かないの……。",0)
+	MES(MINIKINO,"その扉はわたしの力では開かないの……",0)
 	MES_close(MINIKINO)
 
-	MES(MINIKINO,"お父さんたちが\n来てくれるまでは……。",0)
+	MES(MINIKINO,"お父さんたちが\n来てくれるまでは……",0)
 	MES_close(MINIKINO)
 
 	wait(10)
diff --git a/scp_jp_conv/map/6/EV62391.txt b/scp_conv/map/6/EV62391.txt
index 1038cd1..5e9c205 100644
--- a/scp_jp_conv/map/6/EV62391.txt
+++ b/scp_conv/map/6/EV62391.txt
@@ -27,7 +27,7 @@ INIT
 
 //■スイッチ．看板
 	set_chr( 50,620,	 5, 5,  -900,-375,  0,		  0,     0, 0,";")			//①セーブOBJ
-	set_chr( 56,648,	 4, 3,     0, 700,  0,		 19,     0, 0,";")	//レベルプレート
+	set_chr( 56,772,	 4, 3,     0, 700,  0,		 19,     0, 0,";")	//レベルプレート
 		color2( 56, 68,75,86, 0,0,0)
 
 	set_chr( 55,804,	 5, 4,  -525, 650,  0,		  0,   270, 8,"(L2?99 [9991お賽銭＿感謝の心で＿倍返し] WT?30 L2!99 [9903] WT?30);")	//②看板
