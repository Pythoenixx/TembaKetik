-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2024 at 04:29 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tembaketik`
--

-- --------------------------------------------------------

--
-- Table structure for table `accuracy`
--

CREATE TABLE `accuracy` (
  `ID` int(11) NOT NULL,
  `miss_ID` int(11) DEFAULT NULL,
  `WPM_ID` int(11) DEFAULT NULL,
  `percentage` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accuracy`
--

INSERT INTO `accuracy` (`ID`, `miss_ID`, `WPM_ID`, `percentage`) VALUES
(1, 1, 1, '85.29'),
(2, 2, 2, '92.73'),
(3, 3, 3, '92.31'),
(4, 4, 4, '83.33'),
(5, 5, 5, '73.68'),
(6, 6, 6, '86.84'),
(7, 7, 7, '98.04'),
(8, 8, 8, '96.67'),
(9, 9, 9, '90.91'),
(10, 10, 10, '82.42'),
(11, 11, 11, '90.00'),
(12, 12, 12, '85.71'),
(13, 13, 13, '82.19'),
(14, 14, 14, '84.54'),
(15, 15, 15, '93.55'),
(16, 16, 16, '90.63'),
(17, 17, 17, '100.00'),
(18, 18, 18, '100.00'),
(19, 19, 19, '92.31'),
(20, 20, 20, '100.00'),
(21, 21, 21, '100.00'),
(22, 22, 22, '100.00'),
(23, 23, 23, '100.00'),
(24, 24, 24, '100.00'),
(25, 25, 25, '76.92'),
(26, 26, 26, '100.00'),
(27, 27, 27, '100.00'),
(28, 28, 28, '100.00'),
(29, 29, 29, '100.00'),
(30, 30, 30, '100.00'),
(31, 31, 31, '100.00'),
(32, 32, 32, '100.00'),
(33, 33, 33, '75.00'),
(34, 34, 34, '91.43'),
(35, 35, 35, '100.00'),
(36, 36, 36, '100.00'),
(37, 37, 37, '97.96'),
(38, 38, 38, '85.56'),
(39, 39, 39, '27.78'),
(40, 40, 40, '25.40'),
(41, 41, 41, '2.56'),
(42, 42, 42, '76.16'),
(43, 43, 43, '47.83'),
(44, 44, 44, '78.10'),
(45, 45, 45, '25.00'),
(46, 46, 46, '100.00'),
(47, 47, 47, '81.25'),
(48, 48, 48, '83.16'),
(49, 49, 49, '90.71'),
(50, 50, 50, '83.50'),
(51, 51, 51, '81.82'),
(52, 52, 52, '90.78'),
(53, 53, 53, '10.00'),
(54, 54, 54, '45.45'),
(55, 55, 55, '61.90'),
(56, 56, 56, '100.00'),
(57, 57, 57, '68.89'),
(58, 58, 58, '91.67'),
(59, 59, 59, '100.00'),
(60, 60, 60, '88.33'),
(61, 61, 61, '84.19'),
(62, 62, 62, '55.24'),
(63, 63, 63, '80.31'),
(64, 64, 64, '86.67'),
(65, 65, 65, '100.00'),
(66, 66, 66, '81.40'),
(67, 67, 67, '79.04'),
(68, 68, 68, '84.63'),
(69, 69, 69, '68.48'),
(70, 70, 70, '81.16'),
(71, 71, 71, '82.54'),
(72, 72, 72, '0.00'),
(73, 73, 73, '86.67'),
(74, 74, 74, '100.00'),
(75, 75, 75, '83.90'),
(76, 76, 76, '81.22'),
(77, 77, 77, '76.11'),
(78, 78, 78, '84.03'),
(79, 79, 79, '72.62'),
(80, 80, 80, '80.86'),
(81, 81, 81, '82.43'),
(82, 82, 82, '82.60'),
(83, 83, 83, '82.69'),
(84, 84, 84, '79.80'),
(85, 85, 85, '78.48'),
(86, 86, 86, '61.36'),
(87, 87, 87, '83.85'),
(88, 88, 88, '79.82'),
(89, 89, 89, '76.15'),
(90, 90, 90, '77.63'),
(91, 91, 91, '69.54'),
(92, 92, 92, '82.35'),
(93, 93, 93, '100.00'),
(94, 94, 94, '78.13'),
(95, 95, 95, '88.83'),
(96, 96, 96, '84.30'),
(97, 97, 97, '86.54'),
(98, 98, 98, '79.62'),
(99, 99, 99, '84.48'),
(100, 100, 100, '83.64'),
(101, 101, 101, '79.71'),
(102, 102, 102, '80.95'),
(103, 103, 103, '78.99'),
(104, 104, 104, '80.09'),
(105, 105, 105, '82.77');

-- --------------------------------------------------------

--
-- Table structure for table `missed`
--

CREATE TABLE `missed` (
  `ID` int(11) NOT NULL,
  `player_ID` int(11) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `words` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `missed`
--

INSERT INTO `missed` (`ID`, `player_ID`, `count`, `words`) VALUES
(1, 1, 15, 'poor,poor,travelling,travelling,travelling,travelling,travelling,eye,eye,eye,lead,lead'),
(2, 1, 4, 'die,blow,thing,thing'),
(3, 1, 1, 'word'),
(4, 1, 3, 'glass,glass,glass'),
(5, 2, 5, 'birth,birth,birth,birth'),
(6, 2, 5, 'hear,hotel'),
(7, 2, 1, ''),
(8, 2, 1, 'zero'),
(9, 2, 3, 'tear,tear'),
(10, 3, 115, 'rich,rich,rich,happening,sorry,reply,twice,twice,watch,discussed,discussed,discussed,discussed,until,until,until,until,until,until,pharmacology,pharmacology,pharmacology,stay,stay,stay,job,job,limited,limited,sky,sky,webster,webster,grow,bath,customs,fever,or,obey,obey,obey,obey,was,catherine,william,fool,read,read,brave,thick,thick,music,music,music,music,music,meeting,meeting,jelly,spoon,spoon,spoon,piano,round,round,round,round,real,real,queen,queen,queen,oil,chair,chair,chair,jelly,jelly,norfolk,norfolk,norfolk,norfolk,norfolk,cheapest,cheapest,cheapest,broadband,broadband,broadband,broadband,broadband'),
(11, 2, 2, 'touch,touch'),
(12, 2, 2, 'stone,stone'),
(13, 2, 75, 'road,road,ship,sharp,sharp,title,title,title,title,title,stay,stay,stay,paragraph,floor,ship,knife,submitted,submitted,submitted,spoon,put,back,shelf,shelf,transexuales,transexuales,transexuales,transexuales,transexuales,glass,even,even,even,way,free,free,free,fast,fast,decided,decided,decided,fever,fever,favourites,favourites,favourites,absolute,absolute,absolute,neck,that,that,that,that,study,study,study,protocols,home,home'),
(14, 2, 15, 'stay,stay,stay,shade,involves,involves'),
(15, 2, 2, 'pig,brown'),
(16, 2, 3, 'bird,bird,wine'),
(17, 2, 0, ''),
(18, 2, 0, ''),
(19, 2, 1, 'water'),
(20, 2, 0, ''),
(21, 2, 0, ''),
(22, 2, 0, ''),
(23, 2, 0, ''),
(24, 2, 0, ''),
(25, 2, 3, 'place,place,place'),
(26, 2, 0, ''),
(27, 2, 0, ''),
(28, 2, 0, ''),
(29, 2, 0, ''),
(30, 2, 0, ''),
(31, 2, 0, ''),
(32, 2, 0, ''),
(33, 2, 7, 'base,cross,jelly'),
(34, 2, 9, 'price,five,professor,month,month,dirty'),
(35, 2, 0, ''),
(36, 2, 0, ''),
(37, 2, 1, 'yell'),
(38, 2, 27, 'dark,dark,dark,dark,as,introductory,introductory,introductory,introductory,introductory,fresh,child,plate,plate,duty,duty,am,drink,drink,drink,drink'),
(39, 2, 52, 'stamp,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood,blood'),
(40, 2, 185, 'usual,usual,knock,penalties,penalties,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox,fox'),
(41, 2, 76, 'real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real,real'),
(42, 2, 103, 'month,month,spoon,spoon,uncle,uncle,just,just,radio,radio,radio,indirect,woman,volunteers,calculations,calculations,calculations,calculations,calculations,deep,deep,rice,lend,lend,lend,lend,weak,few,few,history,history,enemy,enemy,obesity,obesity,obesity,explained,explained,explained,explained,explained,explained,explained,north,steal,steal,steal,yell,late,late,late,late,late,late,late,late,late,late,late,late,late,late,late,late,late,late,late,late,wish,hear,hear,hear,hear,hear,hear,hear,hear,hear,hear'),
(43, 2, 96, 'star,first,first,first,steal,steal,hotel,dream,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,authorization,mind,mind,god'),
(44, 2, 134, 'cross,stand,must,must,north,north,north,north,north,jump,twice,twice,twice,catalyst,get,get,lady,lady,lady,prize,ocean,ocean,bleed,republican,republican,republican,republican,republican,which,which,australia,chair,chair,chair,parliamentary,parliamentary,parliamentary,parliamentary,step,pokemon,area,area,area,area,area,will,will,will,smell,smell,order,order,clear,occupied,lower,lower,jelly,jelly,curriculum,institution,institution,institution,institution,institution,institution,institution,drink,drink,drink,drink,soap,soap,soap,soap,soap,still,still,still,still,soup,store,store,store,motivation,motivation,motivation,motivation,achievement,achievement,achievement,achievement,achievement'),
(45, 2, 33, ''),
(46, 2, 0, ''),
(47, 2, 3, 'early,dead,into'),
(48, 2, 63, 'brave,much,much,leaf,stamp,glass,glass,glass,glass,dream,deposit,overseas,this,this,eye,disease,disease,disease,sound,sound,sound,chamber,chamber,chamber,stamp,stamp,stamp,enter,glad,glad,fork,fork,fork,fork,fork,shelf,draw,draw,bath,bath,weak,calculated,calculated,calculated,calculated,calculated,cool,coat,coat,coat,coat,coat,coat,coat'),
(49, 2, 17, 'near,half,smile,smile,smile,enjoy,reply,reply,reply'),
(50, 2, 17, 'marry,again,walk,lend,lend,lend,green,an,siemens,siemens,siemens,siemens'),
(51, 2, 6, 'dark,salt,dead,dead'),
(52, 2, 13, 'talk,north,voluntary,voluntary,voluntary,voluntary,voluntary,front'),
(53, 2, 27, ''),
(54, 2, 6, ''),
(55, 2, 8, 'call'),
(56, 2, 0, ''),
(57, 2, 14, 'knock,knock'),
(58, 2, 1, ''),
(59, 2, 0, ''),
(60, 2, 7, 'king,shout,shout,shout,shout'),
(61, 2, 117, 'sabah,intim,intim,intim,kita,kita,kita,pekerjaan,pekerjaan,pekerjaan,sikap,sikap,sikap,ini,arwah,kaca,sendiri,sendiri,sendiri,sendiri,tidak,tidak,tidak,kotor,bulan,bulan,bulan,beras,enjoy,here,lend,bencana,bencana,kejujuran,bukan,bukan,bukan,yard,soft,menerima,about,car,were,force,menjaga,menjaga,menjaga,menjaga,fever,fever,fever,mengajar,much,spell,into,into,soap,pink,twice,join,permulaan,permulaan,permulaan,permulaan,tonight,save,save,save,save,sweet,sweet,sweet,block,block,shout,shout,hope,hope,expensive,expensive,expensive,expensive,twice,twice,stop,examination,examination'),
(62, 2, 47, 'ianya,ianya,sabah,susu,susu,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know,know'),
(63, 2, 113, 'juice,juice,sibuk,sibuk,sheep,sheep,wide,wide,wide,peace,peace,peace,well,increase,increase,increase,start,start,start,clear,clear,clear,clear,than,main,main,main,three,tuntutan,picture,one,feed,since,since,rimba,rimba,rimba,and,peace,peace,mengajar,mengajar,mengajar,perenggan,perenggan,perenggan,perenggan,tikus,tikus,tikus,tikus,tikus,tarik,sedih,kuda,kagum,walaupun,mengalir,mengalir,mengalir,batuk,batuk,batuk,batuk,telah,telah,perak,Pulau,Pulau,Pulau,bagi,menyeberangi,menyeberangi,menyeberangi,menyeberangi,menyeberangi,bulu,menyambung,menyambung,sen,sen,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,menyelamatkan,arwah,arwah'),
(64, 2, 2, 'sedih,sedih'),
(65, 2, 0, ''),
(66, 2, 146, 'store,cloth,cloth,force,force,force,hers,deep,deep,ready,ready,ready,libraries,libraries,libraries,libraries,libraries,libraries,libraries,libraries,stone,stone,stone,stone,today,fault,fault,fault,fault,half,half,half,obesity,obesity,obesity,obesity,obesity,obesity,earn,earn,gray,miss,miss,enter,acdbentity,iron,birth,birth,preparing,preparing,preparing,clock,clock,shape,too,too,shirt,shirt,trinity,smell,chair,chair,sell,lazy,block,block,block,offer,over,over,arm,city,radio,reflects,reflects,reflects,southeast,southeast,southeast,philosophy,philosophy,hold,hold,lend,lend,lend,lend,juice,were,step,andrews,contributed,mechanisms,news,news,news,white,white,else,else,pleasure,pleasure,pleasure,cross,cross,cross,cross,boil,boil,low,low,low,car,car,medicines,half,fool,fool,fool'),
(67, 2, 193, 'blood,today,today,today,today,heavy,immunology,news,ocean,enemy,enemy,enemy,enemy,enemy,tea,tea,tea,third,thing,thing,surveillance,surveillance,surveillance,agree,point,point,point,point,point,point,paint,platform,begin,begin,hide,hide,hide,below,below,copyright,copyright,copyright,launched,launched,launched,launched,carry,carry,carry,carry,vietnam,vietnam,next,stockings,stockings,slip,slip,slip,left,left,left,arm,arm,arm,arm,own,own,own,own,turning,ring,ring,ring,heavy,confused,confused,confused,confused,confused,confused,aunt,aunt,aunt,left,step,recognition,recognition,recognition,recognition,recognition,recognition,recognition,rise,rise,hurt,hurt,six,six,lend,uncle,burn,burn,burn,burn,force,force,chelsea,near,dish,dish,dish,sound,sound,sound,salt,salt,radio,radio,contributors,discharge,discharge,discharge,discharge,discharge,discharge,mean,mean,mean,enemy,enemy,enemy,enemy,an,an,study,study,tablets,park,ride,ride,ride,house,bank,bank'),
(68, 1, 81, 'eye,than,than,wear,twice,twice,usual,moon,left,sharp,sharp,lend,lend,was,was,cheap,cheap,cheap,cheap,carry,carry,must,must,where,where,next,next,reach,reach,force,force,gilbert,gilbert,gilbert,sorry,sorry,sorry,sorry,sharp,leisure,investigators,investigators,investigators,investigators,investigators,high,high,hearing,hearing,best,pain,pain,pain,wait,gift,gift,plugins,plugins,plugins,plugins,bumi,bumi,bumi,permulaan,permulaan,permulaan,permulaan,instrumen,sikap,apa,dari,dari,dari,dari'),
(69, 2, 29, 'sock,sock,sock,sock,sock,sock,sock,sock,sock,sock,sock,sock,sock,sock,sock,bagi'),
(70, 2, 13, 'voice,chase,chase,chase,save,save,pressure,pressure,pressure'),
(71, 2, 158, 'bean,bean,bean,bean,heavy,heavy,mouth,clear,passage,passage,liberia,liberia,liberia,liberia,list,list,road,road,road,blue,blue,innovation,innovation,innovation,innovation,innovation,innovation,innovation,false,false,false,same,same,heart,advertising,advertising,salt,salt,salt,exploration,four,pink,conservative,conservative,conservative,conservative,conservative,conservative,conservative,sunny,total,film,steal,steal,fit,fit,fit,fine,wire,wire,wet,wet,wet,wet,wake,expenditure,enjoy,enjoy,miss,team,float,medicines,medicines,members,members,fear,grenada,grenada,grenada,wear,wear,dust,dust,angry,five,five,shape,shape,sweet,sweet,identifying,identifying,publish,seven,sing,sing,look,look,blow,blow,hair,hair,showing,partition,partition,partition,partition,partition,partition,carrier,chair,chair,camcorder,camcorder,camcorder,quick,prize,prize,prize,shade,subsidiary,subsidiary,subsidiary,subsidiary,organised,organised'),
(72, 2, 152, ''),
(73, 2, 2, 'until'),
(74, 2, 0, ''),
(75, 4, 85, 'front,front,front,safe,party,else,copyrights,copyrights,copyrights,copyrights,copyrights,copyrights,two,child,child,child,compiler,book,book,path,path,small,best,best,freebsd,freebsd,freebsd,limau,limau,tidak,tidak,tidak,tidak,tidak,kemenangan,penyusunan,penyusunan,penyusunan,biru,menghantar,menghantar,sedih,sedih,sedih,sedih,sedih,sedih,putih,perubahan,intim,berbeza-beza,berbeza-beza,berbeza-beza,berbeza-beza,telah,telah,telah,telah,kipas,kipas,untuk,yang,murni,gelas,gelas,gelas,gelas,gelas'),
(76, 2, 102, 'piano,piano,shape,shape,gray,gray,ago,pan,total,meet,meet,cross,cross,cross,fit,fit,fit,sitting,sitting,martial,martial,martial,touch,assuming,assuming,safe,walk,walk,walk,revenues,revenues,storm,storm,storm,storm,storm,sunny,sunny,sunny,sunny,real,spotlight,safe,fine,fine,fine,fine,fine,space,space,lose,hukuman,hukuman,bagi,bagi,batuk,kebal,kebal,kebal,kebal,kebal,kaca,kaca,kaca,kaca,nila,kotor,beras,beras,tidak,tidak'),
(77, 2, 210, 'kebal,kebal,kebal,sikap,sikap,sikap,tasek,tasek,sihat,sihat,padi,padi,padi,padi,ianya,ianya,gelas,sedih,sedih,sedih,seksyen,seksyen,seksyen,seksyen,seksyen,tikus,tikus,tikus,tikus,gajah,rimba,rimba,rimba,hijau,hijau,hijau,hijau,hijau,sedih,sedih,sedih,perjuangan,ombak,ombak,mati,mati,mati,mati,lain,untuk,untuk,untuk,saya,menambah,menambah,menambah,menambah,menambah,kebal,kebal,kebal,guruh,guruh,guruh,bintang,bintang,bintang,bintang,bintang,mengandungi,mengandungi,mengandungi,mengandungi,kaler,cina,cina,air,air,air,air,air,jantung,jantung,tahun,tahun,tahun,perubahan,perubahan,tidak,tidak,rimba,rimba,tahun,tahun,lebat,lebat,lebat,membolehkan,membolehkan,membolehkan,membolehkan,kegembiraan,kegembiraan,pakaian,pakaian,serta,susu,susu,teh,teh,teh,pihak,pihak,tasek,masa,wang,wang,gajah,gajah,perempuan,perempuan,perempuan,terlibat,terlibat,terlibat,lalat,lalat,hari,hari,hari,tasek,saya,saya,apa,ketulusan,ketulusan,ketulusan,mengharapkan,kita,kita,diri,diri,ini,ini,ini,ini,ini,ini,ini,ini,sibuk,sibuk,sibuk,amat,kita,kita,kita,kita,pupuk,beras,intim,sabah,sabah,cina,permukaan,permukaan,permukaan,tentera,tentera,perlawanan'),
(78, 2, 19, 'batuk,hijau,hijau,kedudukan,untuk,untuk,untuk,untuk,untuk,kita,kita,kita,kita,kita'),
(79, 2, 276, 'bleed,bleed,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,white,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,reliable,space,space,space,space,space,space,space,space,space,space,space,space,exact,exact,exact,exact,exact,exact,exact,exact,exact,easy,easy,easy,easy,easy,easy,easy,iron,iron,iron,iron,iron,iron,iron,iron,iron,iron,iron,point,point,point,point,point,point,point,point,point,point,point,point,point,plate,plate,noble,noble,noble,packaging,packaging,spell,bank,bank,sad,eight,eight,eight,pink,enemy,enemy,occurring,occurring,fill,fill,secretary,secretary,secretary,secretary,secretary,secretary,blood,volleyball,volleyball,volleyball,salt,situation,situation,situation,situation,take,take,dirty,dirty,dirty,dirty,dirty,dirty,tram,tram,piano,piano,increasing,increasing,confirm,confirm,confirm,page,page,power,power,power,burn,burn,burn,paper,paper,progressive,progressive,progressive,progressive,progressive,hope,hope,hope,raise,into,into,into,businesses,businesses,businesses,ownership,ownership,programming,programming,programming,programming,star,star,black,black,black,next,box,box,komputer,tidak,tarik,tarik,tolak,tolak,yang,lebat,lebat,bukan,hijau,hijau,lalat,lalat,telah,telah'),
(80, 2, 129, 'taste,taste,taste,pupil,with,with,with,with,spell,westminster,westminster,abortion,abortion,shake,funny,funny,good,to,to,paintball,paintball,paintball,paintball,noise,noise,noise,differences,eye,eye,eye,be,rush,rush,rush,red,corn,approval,nose,rich,rich,life,cheap,washington,heavy,desperate,desperate,desperate,desperate,desperate,desperate,type,type,test,bite,bite,bite,pair,pair,book,bleed,barbara,mind,list,list,star,star,essentials,essentials,essentials,essentials,essentials,pediatric,pediatric,pediatric,accepting,accepting,yell,lamp,burn,burn,burn,burn,fault,fit,fit,fit,fit,act,act,act,act,act,act,banking,push,push,push,push,grow,surveillance,surveillance,surveillance,surveillance'),
(81, 2, 39, 'pick,pick,ride,flat,start,start,plant,south,south,south,shine,rainy,surprising,surprising,shop,ship,join,stephanie,stephanie,stephanie,stephanie,stephanie,stephanie,stephanie,stephanie,stephanie,stephanie,offer,offer,offer,quiet,quiet'),
(82, 2, 135, 'draw,other,other,barriers,carry,lead,lead,lead,lead,alpa,alpa,alpa,itu,itu,bagi,bagi,bagi,bagi,tasek,perempuan,perempuan,hutan,sirap,sirap,tidak,membiak,membiak,kotor,kotor,kotor,kotor,dalam,kelebihan,ingin,masa,membantu,gempa,guruh,teh,bulan,lebat,Pulau,Pulau,Pulau,saya,kaler,murni,lebat,lebat,lebat,tidak,tidak,guruh,guruh,gelombang,gelombang,gelombang,membimbing,membimbing,membimbing,membaca,lalat,lalat,sen,sen,sen,dan,kuda,oren,padi,padi,padi,pelajaran,basikal,basikal,bumi,bumi,bukan,sirap,sirap,sirap,kita,sibuk,ianya,ianya,menimbulkan,menimbulkan,menimbulkan,menimbulkan,menimbulkan,menimbulkan,menimbulkan,menimbulkan,menimbulkan,menimbulkan'),
(83, 2, 27, 'title,title,title,title,paper,paper,paper,paper,steam,menyentuh,menyentuh,bulu,bulu,mengesan,mengesan,ask,ask'),
(84, 2, 182, 'brave,third,piece,piece,piece,wait,wait,wait,drop,drop,drop,title,cost,cost,cost,eat,chair,chair,chair,chair,chair,cross,cross,eight,eight,pain,kind,demonstrate,demonstrate,demonstrate,demonstrate,demonstrate,demonstrate,on,on,woman,woman,north,normally,normally,normally,normally,normally,viewpicture,fresh,music,reply,reply,reply,ship,fault,fault,fault,fault,fault,fault,deer,deer,deer,fresh,fresh,poverty,boat,thing,thing,understood,rule,rule,rule,rule,own,own,own,own,pay,pay,many,many,catch,catch,catch,block,block,week,week,engines,engines,engines,experiencing,experiencing,experiencing,experiencing,three,or,order,order,digital,digital,moon,from,from,from,stop,drop,drop,drop,drop,drop,ruler,ruler,replica,replica,replica,parliamentary,simulations,simulations,lady,lady,lady,lady,ready,ready,since,since,since,size,size,same,wake,wait,wait,serving,boil,boil,boil,boil,boil,boil,big,big,big,brush,brush,god,god,god,identity'),
(85, 2, 68, 'right,right,juice,juice,world,cross,cross,own,own,own,own,offer,offer,offer,press,additional,additional,additional,additional,story,ocean,supports,catch,other,luck,luck,luck,luck,luck,luck,luck,true,true,popularity,popularity,popularity,sail,sail,sail,outstanding,outstanding,outstanding,outstanding,foot,foot,foot,characteristic,characteristic'),
(86, 2, 1809, ''),
(87, 2, 21, 'bag,event,event,event,cold,cold,cold,taxi,taxi,taxi,bring,sand,hopefully,hopefully,hopefully,hopefully,hopefully,hopefully,hopefully,flag,flag'),
(88, 2, 114, 'wide,safe,safe,tear,tear,usual,usual,usual,mind,speed,speed,speed,pekerja,grass,swim,plate,window,iron,iron,moon,floor,antarabangsa,antarabangsa,piece,piece,piece,piece,pan,sleep,grass,mempopulasikan,mempopulasikan,gate,mencapai,mencapai,perhatian,perhatian,plastik,plastik,type,type,earth,earth,corn,along,along,along,along,along,these,these,too,too,obey,obey,obey,obey,obey,obey,obey,obey,own,own,own,petrol,petrol,petrol,queen,queen,queen,study,study,india,india,earth,earth,earth,earth,earth,earth,earth,earth'),
(89, 2, 177, 'drop,what,what,bath,bath,villages,stay,stay,stay,stay,stay,stay,stay,stay,watch,form,form,form,north,north,north,north,north,north,meal,east,east,east,dance,dance,dance,dance,dance,duty,duty,ianya,ianya,sekolah,sekolah,perak,tarik,tarik,amat,ada,ada,nasi,nasi,nasi,lembu,lembu,perenggan,perenggan,perenggan,perenggan,wang,wang,diri,permaisuri,bagi,bagi,sedih,sedih,sedih,sedih,sedih,sedih,dapat,pendahuluan,pendahuluan,pendahuluan,pendahuluan,pendahuluan,pendahuluan,pendahuluan,pendahuluan,pendahuluan,lalat,intim,intim,biru,biru,biru,meminta,meminta,telah,lalat,awak,ciku,sabah,ianya,ianya,pemeriksaan,pemeriksaan,pemeriksaan,pemeriksaan,pemeriksaan,membincangkan,berharap,berharap,berharap,berharap,berharap,saya,tidak,tidak,tidak,saudara,saudara,saudara,kepentingan,kepentingan,kepentingan,petir,insiden,insiden,insiden,hijau,hijau,hijau,bumi,bumi,beras,hari,tarik,tarik,tarik,hari,menghasilkan,menghasilkan,menghasilkan,menghasilkan,menghasilkan,menghasilkan,menghasilkan,menghasilkan'),
(90, 2, 174, 'rich,rich,brown,bean,bean,stay,stay,stay,water,water,open,am,am,am,other,other,other,other,other,other,ruler,bank,bank,coin,investment,investment,investment,usual,usual,divided,divided,divided,divided,divided,divided,divided,each,each,accident,son,son,exact,exact,exact,what,what,sock,bird,mechanisms,mechanisms,me,me,tool,make,make,make,comparisons,comparisons,comparisons,comparisons,comparisons,starsmerchant,starsmerchant,starsmerchant,starsmerchant,today,today,today,sound,tobacco,transaction,transaction,transaction,transaction,transaction,kind,kind,kind,rochester,juice,juice,juice,juice,juice,come,come,come,shout,shout,shout,shout,shape,knee,equipped,equipped,equipped,returned,returned,returned,returned,returned,returned,equipment,equipment,equipment,waste,waste,knock,knock,juice,gray,lebanon,lebanon,houston,houston,about,about,radio,radio,radio,radio,increases,increases,tremendous,tremendous,piece,piece,piece,such,such,such,milk,milk,milk,music,music,music,music,hope,month,month,head,head,head'),
(91, 2, 177, 'associate,disciplinary,disciplinary,disciplinary,disciplinary,advisors,advisors,advisors,advisors,advisors,advisors,advisors,estonia,industrial,highlights,highlights,highlights,biggest,biggest,biggest,biggest,biggest,biggest,revised,revised,revised,revised,revised,reproductive,reproductive,reproductive,reproductive,reproductive,reproductive,influence,influence,casinos,casinos,authentic,authentic,authentic,authentic,authentic,authentic,obituaries,obituaries,obituaries,consisting,dollars,dollars,dollars,dollars,dollars,dollars,website,website,pharmaceutical,backing,insertion,insertion,insertion,insertion,stations,stations,stations,stations,stations,stations,stations,stations,stations,stations,disabilities,disabilities,disabilities,disabilities,disabilities,disabilities,disabilities,injection,penggunaan,penggunaan,penggunaan,nasi,nasi,nasi,kotor,kotor,kotor,kotor,kotor,kotor,tahun,tahun,tahun,tahun,serta,serta,serta,serta,serta,serta,hutan,hutan,hutan,yang,sen,sen,limau,limau,limau,limau,tasek,tasek,telah,telah,telah,telah,telah'),
(92, 2, 3, 'piano,piano,piano'),
(93, 2, 0, ''),
(94, 2, 175, 'title,knee,knee,pair,pair,board,board,board,event,mix,title,five,five,five,annotated,annotated,voice,chair,chair,cognitive,cognitive,organization,organization,organization,organization,were,watch,watch,watch,spanish,spanish,their,their,their,their,their,god,dirty,dirty,javascript,javascript,javascript,javascript,door,door,rendered,rendered,displaying,displaying,variation,variation,variation,pick,south,south,south,fail,fail,thing,do,early,early,early,early,see,see,see,hard,which,which,which,hole,hole,hole,knee,knee,knee,plate,plate,plate,plate,sky,sky,sky,sky,ask,ask,ask,slip,slip,slip,waste,waste,knock,knock,knock,park,musical,musical,musical,musical,verizon,automobiles,automobiles,automobiles,automobiles,ugly,ugly,ugly,ago,ago,ago,book,book,book,book,slow,slow,slow,hair,hair,influences,influences,influences,influences,enquiry,enquiry,enquiry,enquiry,enquiry,so,so,so,horse,horse,horse,push,push'),
(95, 13, 21, 'flag,voice,modified,fact,fact,blood,blood,sweet,fine,best,best'),
(96, 13, 38, 'three,sand,winning,bone,floor,two,processed,die,leaf,paper,paper,paper,next,recovered,recovered,recovered,put,put,put,put,put,blood,blood'),
(97, 13, 35, 'clear,black,float,float,float,float,float,card,fast,fast,goat,goat,need,duty,duty,conversation,conversation,duck,dream,sell,sell,cost,cost,cost,than,net,net,two'),
(98, 13, 32, 'many,many,many,many,many,sunny,event,event,event,event,event,event,fox,fox,administered,administered,government,government,government,government,government,government,government,government,sleep'),
(99, 13, 52, 'ask,these,pig,pig,pig,specials,specials,lion,lion,learn,five,five,five,five,five,five,enemy,enemy,get,get,fine,close,close,close,close,close,hot,streets,streets,fox,fox,fox,fox,hope,hope,hope'),
(100, 13, 45, 'slip,slip,slip,slip,slip,land,along,along,along,less,less,less,less,last,nashville,smile,smile,smile,smile,smile,part,networks,networks,green,gray,feed,tidy,marry,marry,marry,clear,clear,clear,clear,clear,clear,quiet'),
(101, 13, 42, 'smoke,smoke,smoke,smoke,smoke,sugar,ship,ship,town,dance,dance,auckland,auckland,auckland,auckland,auckland,milk,milk,milk,news,news,news,place,place,place,place,place,place,floor,else,else,glad,glad,reservations,reservations,reservations,table,ship'),
(102, 2, 173, 'love,love,love,teach,leaf,conclude,conclude,conclude,conclude,each,whether,whether,whether,whether,whether,whether,whether,whether,whether,whether,whether,cloth,cloth,noise,taste,taste,taste,earn,earn,corn,empty,right,right,right,right,form,form,bird,bird,spell,spell,spell,catch,ear,auction,auction,auction,auction,auction,auction,auction,correctly,correctly,week,week,ability,need,need,pain,pain,pain,near,hen,hen,hen,hen,ready,earth,warrant,warrant,room,room,shape,shape,shape,shape,shape,tie,tie,fairfield,fairfield,fairfield,fairfield,fairfield,fairfield,fairfield,prospective,prospective,prospective,prostate,prostate,prostate,prostate,busy,eat,enjoy,appearing,appearing,appearing,appearing,appearing,spoon,queen,own,own,ocean,fork,fork,fork,young,young,above,above,even,even,businesses,businesses,businesses,businesses,businesses,interventions,interventions,cross,cross,cross,good,good,permissions,permissions,permissions,try,much,much,born,born,born,happy,happy,magazine,magazine,magazine'),
(103, 2, 25, 'share,share,share,first,visit,cake,month,month,quiet,quiet,preview,preview,preview,below,below,below,paper,paper,paper,paper,paper,paper'),
(104, 2, 93, 'chase,chase,chase,chase,chase,referring,referring,referring,referring,referring,referring,dance,eat,eat,eat,have,have,reliable,sweet,lower,lower,pay,weekends,weekends,third,third,pour,pour,juice,half,half,heart,less,less,less,keywords,lawsuit,lawsuit,lawsuit,lawsuit,lawsuit,lawsuit,head,since,since,force,white,glossary,glossary,accomplish,is,earth,earth,earth,earth,earth,unavailable,rude,rude,hard,hard,fresh,dish,dish,birth,birth,birth,birth,quantities,quantities,quantities,quantities,bear,bear'),
(105, 2, 112, 'lot,lot,count,count,count,burn,burn,tooth,webmasters,webmasters,resulting,resulting,great,great,great,brush,brush,brush,brush,brush,mississippi,mississippi,mississippi,tool,die,save,save,save,wear,wear,wear,wear,definitely,definitely,definitely,definitely,sun,sun,sun,twice,room,early,early,early,not,not,labeled,labeled,labeled,quick,quick,quick,requiring,requiring,requiring,cloud,cloud,cloud,neck,neck,neck,neck,neck,neck,storm,storm,just,just,mind,ocean,ocean,ocean,memories,memories,voltage,noise,noise,fault,fault,ship,ship,ship,ship,ericsson,ericsson,ericsson,ericsson,ericsson,ericsson');

-- --------------------------------------------------------

--
-- Table structure for table `player`
--

CREATE TABLE `player` (
  `ID` int(11) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `player`
--

INSERT INTO `player` (`ID`, `Username`, `Password`) VALUES
(1, 'Pythoenix', 'yatagarasu'),
(2, 'a', 'a'),
(3, 't', 't'),
(4, 'yatagarasuuiii', 'yatagarasu'),
(10, 'urmom', 'urmom'),
(13, 'FIYREX', '1912');

-- --------------------------------------------------------

--
-- Table structure for table `score`
--

CREATE TABLE `score` (
  `miss_ID` int(11) NOT NULL,
  `accuracy_ID` int(11) NOT NULL,
  `WPM_ID` int(11) NOT NULL,
  `nilai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `score`
--

INSERT INTO `score` (`miss_ID`, `accuracy_ID`, `WPM_ID`, `nilai`) VALUES
(1, 1, 1, 1316),
(2, 2, 2, 1250),
(3, 3, 3, 1029),
(4, 4, 4, 872),
(5, 5, 5, 786),
(6, 6, 6, 1111),
(7, 7, 7, 1210),
(8, 8, 8, 1164),
(9, 9, 9, 1194),
(10, 10, 10, 3165),
(11, 11, 11, 1167),
(12, 12, 12, 1024),
(13, 13, 13, 2271),
(14, 14, 14, 1167),
(15, 15, 15, 1176),
(16, 16, 16, 1078),
(17, 17, 17, 533),
(18, 18, 18, 521),
(19, 19, 19, 511),
(20, 20, 20, 537),
(21, 21, 21, 1088),
(22, 22, 22, 504),
(23, 23, 23, 533),
(24, 24, 24, 512),
(25, 25, 25, 426),
(26, 26, 26, 529),
(27, 27, 27, 504),
(28, 28, 28, 504),
(29, 29, 29, 504),
(30, 30, 30, 504),
(31, 31, 31, 504),
(32, 32, 32, 504),
(33, 33, 33, 649),
(34, 34, 34, 1170),
(35, 35, 35, 512),
(36, 36, 36, 654),
(37, 37, 37, 898),
(38, 38, 38, 1334),
(39, 39, 39, 505),
(40, 40, 40, 688),
(41, 41, 41, 21),
(42, 42, 42, 2121),
(43, 43, 43, 864),
(44, 44, 44, 2777),
(45, 45, 45, 171),
(46, 46, 46, 537),
(47, 47, 47, 460),
(48, 48, 48, 1970),
(49, 49, 49, 1502),
(50, 50, 50, 1151),
(51, 51, 51, 977),
(52, 52, 52, 1440),
(53, 53, 53, 62),
(54, 54, 54, 248),
(55, 55, 55, 419),
(56, 56, 56, 696),
(57, 57, 57, 702),
(58, 58, 58, 504),
(59, 59, 59, 550),
(60, 60, 60, 967),
(61, 61, 61, 3410),
(62, 62, 62, 892),
(63, 63, 63, 2731),
(64, 64, 64, 895),
(65, 65, 65, 615),
(66, 66, 66, 3463),
(67, 67, 67, 3818),
(68, 68, 68, 2662),
(69, 69, 69, 841),
(70, 70, 70, 1034),
(71, 71, 71, 3964),
(72, 72, 72, 0),
(73, 73, 73, 895),
(74, 74, 74, 1161),
(75, 75, 75, 2673),
(76, 76, 76, 2665),
(77, 77, 77, 3583),
(78, 78, 78, 1212),
(79, 79, 79, 3830),
(80, 80, 80, 3114),
(81, 81, 81, 1442),
(82, 82, 82, 3491),
(83, 83, 83, 1224),
(84, 84, 84, 3853),
(85, 85, 85, 1820),
(86, 86, 86, 13153),
(87, 87, 87, 1097),
(88, 88, 88, 2728),
(89, 89, 89, 3174),
(90, 90, 90, 3297),
(91, 91, 91, 2534),
(92, 92, 92, 1015),
(93, 93, 93, 537),
(94, 94, 94, 3457),
(95, 95, 95, 1366),
(96, 96, 96, 1547),
(97, 97, 97, 1632),
(98, 98, 98, 1171),
(99, 99, 99, 1893),
(100, 100, 100, 1639),
(101, 101, 101, 1346),
(102, 102, 102, 3933),
(103, 103, 103, 1176),
(104, 104, 104, 2440),
(105, 105, 105, 3066);

-- --------------------------------------------------------

--
-- Table structure for table `wpm`
--

CREATE TABLE `wpm` (
  `ID` int(11) NOT NULL,
  `player_ID` int(11) DEFAULT NULL,
  `typed_word_count` int(11) DEFAULT NULL,
  `nilai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wpm`
--

INSERT INTO `wpm` (`ID`, `player_ID`, `typed_word_count`, `nilai`) VALUES
(1, 1, 87, 76),
(2, 1, 51, 83),
(3, 1, 12, 75),
(4, 1, 15, 57),
(5, 2, 14, 52),
(6, 2, 33, 78),
(7, 2, 50, 74),
(8, 2, 29, 81),
(9, 2, 30, 89),
(10, 3, 539, 71),
(11, 2, 18, 93),
(12, 2, 12, 79),
(13, 2, 346, 59),
(14, 2, 82, 58),
(15, 2, 29, 85),
(16, 2, 29, 73),
(17, 2, 8, 0),
(18, 2, 5, 0),
(19, 2, 12, 0),
(20, 2, 9, 0),
(21, 2, 25, 70),
(22, 2, 1, 0),
(23, 2, 8, 0),
(24, 2, 3, 0),
(25, 2, 10, 0),
(26, 2, 7, 0),
(27, 2, 1, 0),
(28, 2, 1, 0),
(29, 2, 1, 0),
(30, 2, 1, 0),
(31, 2, 1, 0),
(32, 2, 1, 0),
(33, 2, 21, 27),
(34, 2, 96, 45),
(35, 2, 3, 0),
(36, 2, 17, 12),
(37, 2, 48, 30),
(38, 2, 160, 34),
(39, 2, 20, 41),
(40, 2, 63, 43),
(41, 2, 2, 0),
(42, 2, 329, 52),
(43, 2, 88, 37),
(44, 2, 478, 55),
(45, 2, 11, 0),
(46, 2, 9, 0),
(47, 2, 13, 0),
(48, 2, 311, 36),
(49, 2, 166, 51),
(50, 2, 86, 54),
(51, 2, 27, 66),
(52, 2, 128, 65),
(53, 2, 3, 0),
(54, 2, 5, 0),
(55, 2, 13, 8),
(56, 2, 9, 23),
(57, 2, 31, 33),
(58, 2, 11, 0),
(59, 2, 12, 0),
(60, 2, 53, 44),
(61, 2, 623, 54),
(62, 2, 58, 54),
(63, 2, 461, 57),
(64, 2, 13, 59),
(65, 2, 11, 10),
(66, 2, 639, 54),
(67, 2, 728, 53),
(68, 1, 446, 53),
(69, 2, 63, 34),
(70, 2, 56, 57),
(71, 2, 747, 60),
(72, 2, 0, 0),
(73, 2, 13, 59),
(74, 2, 13, 88),
(75, 4, 443, 57),
(76, 2, 441, 59),
(77, 2, 669, 57),
(78, 2, 100, 54),
(79, 2, 732, 57),
(80, 2, 545, 61),
(81, 2, 183, 38),
(82, 2, 641, 56),
(83, 2, 129, 39),
(84, 2, 719, 63),
(85, 2, 248, 56),
(86, 2, 2873, 113),
(87, 2, 109, 32),
(88, 2, 451, 63),
(89, 2, 565, 61),
(90, 2, 604, 54),
(91, 2, 404, 71),
(92, 2, 14, 79),
(93, 2, 9, 0),
(94, 2, 625, 64),
(95, 13, 167, 32),
(96, 13, 204, 39),
(97, 13, 225, 37),
(98, 13, 125, 36),
(99, 13, 283, 41),
(100, 13, 230, 37),
(101, 13, 165, 37),
(102, 2, 735, 64),
(103, 2, 94, 56),
(104, 2, 374, 68),
(105, 2, 538, 57);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accuracy`
--
ALTER TABLE `accuracy`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `miss_ID` (`miss_ID`),
  ADD KEY `WPM_ID` (`WPM_ID`);

--
-- Indexes for table `missed`
--
ALTER TABLE `missed`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `player_ID` (`player_ID`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `score`
--
ALTER TABLE `score`
  ADD PRIMARY KEY (`miss_ID`,`accuracy_ID`,`WPM_ID`),
  ADD KEY `accuracy_ID` (`accuracy_ID`),
  ADD KEY `WPM_ID` (`WPM_ID`);

--
-- Indexes for table `wpm`
--
ALTER TABLE `wpm`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `player_ID` (`player_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accuracy`
--
ALTER TABLE `accuracy`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT for table `missed`
--
ALTER TABLE `missed`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT for table `player`
--
ALTER TABLE `player`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `wpm`
--
ALTER TABLE `wpm`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accuracy`
--
ALTER TABLE `accuracy`
  ADD CONSTRAINT `accuracy_ibfk_1` FOREIGN KEY (`miss_ID`) REFERENCES `missed` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `accuracy_ibfk_2` FOREIGN KEY (`WPM_ID`) REFERENCES `wpm` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `missed`
--
ALTER TABLE `missed`
  ADD CONSTRAINT `missed_ibfk_1` FOREIGN KEY (`player_ID`) REFERENCES `player` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `score`
--
ALTER TABLE `score`
  ADD CONSTRAINT `score_ibfk_1` FOREIGN KEY (`miss_ID`) REFERENCES `missed` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `score_ibfk_2` FOREIGN KEY (`accuracy_ID`) REFERENCES `accuracy` (`ID`) ON DELETE CASCADE,
  ADD CONSTRAINT `score_ibfk_3` FOREIGN KEY (`WPM_ID`) REFERENCES `wpm` (`ID`) ON DELETE CASCADE;

--
-- Constraints for table `wpm`
--
ALTER TABLE `wpm`
  ADD CONSTRAINT `wpm_ibfk_1` FOREIGN KEY (`player_ID`) REFERENCES `player` (`ID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
