# psyphen written by Benjamin Jack Cullen

import os
import csv
import time
import codecs
import distutils.dir_util
import shutil
import subprocess

audext = [".3gp", ".aa", ".aac", ".aax", ".act", ".aiff", ".amr", ".ape", ".au",
            ".awb", ".dct", ".dss", ".dvf", ".flac", ".gsm", ".iklax", ".ivs", ".m4a", ".m4b",
            ".m4p", ".mmf", ".mp3", ".mpc", ".msv", ".ogg", ".oga", ".opus", ".ra", ".rm", ".raw",
            ".sln", ".tta", ".vox", ".wav", ".wma", ".wv", ".webm"]

imgext = [".png", ".jpg", ".jpeg", ".gif", ".ico", ".bmp", ".jpeg2000", ".exif",
    ".tiff", ".tif", ".ppm", ".pgm", ".pbm", ".pnm", ".webp", ".hdr", ".heif", ".cd5",
    ".deep", ".ecw", ".fits", ".flif", ".ilbm", ".img", ".jpegxr", ".nrrd", ".pam",
    ".pcx", ".pgf", ".plbm", ".sgi", ".sid", ".tga", ".targa", ".vicar", ".nasa", ".jpl",
    ".cpt", ".psd", ".xcf", ".iso", ".iec", ".svg", ".dxf", ".cdr", ".ai", ".xml", ".hpgl",
    ".hvif", ".mathml", ".naplps", ".odg", ".draw", ".ppt", ".vml", ".wmf", ".emf", ".xar",
    ".xps", ".blend", ".dgn", ".dwf", ".dwg", ".dxf", ".flt", ".ma", ".mb", ".obj", ".3d",
    ".3dm", ".3ds", ".ani", ".anim", ".apng", ".art", ".bsave", ".cal", ".cin", ".cpc",
    ".cpt", ".dds", ".dpx", ".ecw", ".exr", ".ff", ".fits", ".flic", ".flif", ".fpx",
    ".hdri", ".hevc", ".icer", ".icns", ".cur", ".ics", ".ilbm", ".jbig", ".jibig2", ".jng",
    ".jpeg-ls", ".mng", ".miff", ".nrrd", ".pcx", ".pgf", ".pictor", ".psd", ".psb", ".qtvr",
    ".ras", ".rbe", ".jpeg-hdr", ".wbmp", ".webp", ".xbm", ".xcf", ".xpm", ".xwd", ".ciff",
    ".dng", ".cgm", ".dxf", ".eva", ".hvif", ".iges", ".pgml", ".svg", ".vml", ".cdf",
    ".djvu", ".eps", ".pdf", ".ps", ".swf", ".xaml"]

txtext = [".srt", ".ris", ".asc", ".vmg", ".cm0013", ".enc", ".ass", ".tbl", ".sub", ".html",
    ".htm", ".pts", ".csv", ".conf", ".wrl", ".sdnf", ".xfd", ".lst", ".txt", ".xml", ".eia", ".ecsv",
    ".pod", ".1", ".vfk", ".smi", ".pl", ".asp", ".rdf", ".tsv", ".ascii", ".att", ".modd", ".arff",
    ".spx", ".dbt", ".bas", ".text", ".iif", ".textclipping", ".pgw", ".nfo", ".smali", ".rtf", ".ffp",
    ".pdu", ".lst", ".xmp", ".fpt", ".dtd", ".ltx", ".wtf", ".wer", ".manifest", ".xsl", ".tce", ".tt",
    ".fsa", ".xsd", ".las", ".lrc", ".label", ".stf", ".plist", ".aml", ".application", ".12da", ".log",
    ".ARTask", ".opml", ".reg", ".annot", ".xlf", ".alx", ".hwl", ".des", ".ssa", ".brf", ".xlog", ".sfb",
    ".tfw", ".srx", ".diz", ".drp", ".tlx", ".full", ".linix", ".strings", ".yml", ".ver", ".kar", ".bss",
    ".xff", ".cmd", ".extra", ".diskdefines", ".pcl", ".gen", ".eng", ".not", ".fr", ".fin", ".rtx", ".xdp",
    ".md", ".s2k", ".ac", ".notes", ".ipr", ".mtx", ".report", ".blm", ".adl", ".sha1", ".gbf", ".ans",
    ".clg", ".us", ".emulecollection", ".ru", ".mkd", ".lin", ".html5", ".asp", ".ba1", ".s19", ".coo",
    ".etf", ".ansi", ".mf", ".idt", ".txe", ".ssf", ".dqy", ".lnc", ".err", ".resp", ".dat", ".uhtml",
    ".mw", ".igy", ".dea", ".zib", ".efm", ".en", ".dpv", ".dok", ".ja", ".odc", ".rml", ".wsf", ".soap",
    ".readme", ".rff", ".rt", ".st1", ".adt", ".ctl", ".mp3.", ".nbr", ".bpdx", ".uk", ".bog", ".bnx",
    ".pvw", ".ger", ".plk", ".skv", ".crash", ".hz", ".desc", ".sami", ".etx", ".oot", ".srt", ".wir",
    ".android", ".pla", ".nt", ".rus", ".user", ".wst", ".utf8", ".xslt", ".bcr", ".ltr", ".ion",
    ".cof", ".rep", ".wkf", ".usf", ".xy", ".spec", ".cd2", ".markdown", ".de", ".vkp", ".isr", ".dmr",
    ".mit", ".pmo", ".lwd", ".vhdl", ".bdp", ".map", ".vna", ".vw", ".bna", ".frm", ".enf", ".xsr",
    ".new", ".1st", ".xwp", ".thp", ".gnu", ".prc", ".dk", ".adw", ".dkz", ".zhp", ".la", ".dp", ".opc",
    ".vhd", ".bbs", ".vxml", ".nlc", ".bln", ".cdt", ".xdl", ".pin", ".esw", ".hhc", ".ort", ".lxfml",
    ".$00", ".uni", ".mdown", ".$01", ".kor", ".aqt", ".sbv", ".asl", ".zw", ".pjs", ".luf", ".txt",
    ".tx?", ".mvg", ".qdt", ".big", ".jp1", ".rea", ".guide", ".lyr", ".ckn", ".rest", ".tle", ".tmx",
    ".dfe", ".tcm", ".$02", ".awa", ".maxFR", ".htx", ".pla", ".ltt", ".jeb", ".sha512", ".prn", ".bsdl",
    ".it", "._me", ".lisp", ".utx", ".iem", ".crd", ".prr", ".mkdn", ".faq", ".klg", ".dii", ".es",
    ".hvc", ".kix", ".mdwn", ".mcw", ".wsh", ".aiml", ".ncm", ".inuse", ".pc5", ".pd", ".!!!", ".xct",
    ".gthr", ".xco", ".$04", ".edt", ".trn", ".dfm", ".tph", ".txh", ".ttxt", ".mib", ".7", ".ocr",
    ".qud", ".hs", ".lst", ".cc", ".usg", ".ttpl", ".vis", ".rtl", ".wtx", ".lay", ".ctl", ".charset",
    ".first", ".rst", ".x70", ".now", ".hlm", ".$01", ".assoc", ".lyt", ".lo_", ".001", ".blw", ".me",
    ".q&a", ".wn", ".cif", ".atc", ".thml", ".spn", ".idx", ".ddt", ".tab", ".$ol", ".jam", ".man",
    ".mdl", ".tte", ".euc", ".awh", ".seq", ".bk", ".bea", ".ill", ".ht3", ".tm", ".kch", ".fff",
    ".bt", ".gpl", ".dne", ".txd", ".fnx", ".adiumhtmllog", ".mss", ".zed", ".utxt", ".ttf", ".psb",
    ".idc", ".bep", ".hdr", ".ttbl", ".igv", ".mez", ".jtx", ".u3i", ".text", ".hhs", ".lst", ".mar",
    ".clix", ".htmls", ".fmr", ".pbd", ".pfs", ".chord", ".gdt", ".skcard", ".plf", ".$05", ".xhtm",
    ".ted", ".jis", ".ctx", ".xy3", ".txa", ".cmtx", ".edml", ".oh", ".soundscript", ".snw", ".pml",
    ".dectest", ".tlx", ".trt", ".gtx", ".bad", ".sms", ".vet", ".oogl", ".dcd", ".mtx", ".panic", ".dddd",
    ".mathml", ".vw3", ".omn", ".spa", ".xyp", ".big5", ".inc", ".bdr", ".spg", ".xwp", ".lue",
    ".unx", ".ojp", ".tnef", ".x20", ".cs", ".pt3", ".zxe", ".apx", ".t", ".cassembly", ".cli", ".92t",
    ".cmanifest", ".awb", ".tx8", ".tgf", ".nmbd", ".nwctxt", ".x80", ".tlb", ".tdf", ".82t", ".txa",
    ".stq", ".bel", ".id31", ".mpsub", ".unauth", ".x90", ".xyz", ".pro", ".ctf", ".mdtext", ".jss",
    ".sct", ".p3x", ".wrd", ".dsml", ".hp8", ".ctd", ".cag", ".rzn", ".nclk", ".rbdf", ".xyw", ".cas",
    ".t2t", ".xb0", ".uax", ".hlx", ".syn", ".tbd", ".x60", ".id32", ".nokogiri", ".cho", ".openbsd",
    ".box", ".dce", ".dse", ".linx", ".pvj", ".aprj", ".bzw", ".rzk", ".flr", ".axt", ".py"]  # .py here for benjamin :)

vidext = [".webm", ".mkv", ".flv", ".vob", ".ogb", ".ogg", ".gif", ".gifv", ".mng", ".avi",
    ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".asf", ".mp4", ".m4p", ".m4v", ".mpg", ".mp2",
    ".mpeg", ".mpe", ".mpv", ".m2v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".f4v", ".f4p",
    ".f4a", ".f4b"]

exeext = [".exe", ".bat", ".apk"]

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

encode = u'\u5E73\u621015\u200e,'
config = 'config.conf'

wh_path = ''
wh_path_root = ''

aud_dest = ''
img_dest = ''
txt_dest = ''
vid_dest = ''
exe_dest = ''

dir0_set = False
dir1_set = False
dir2_set = False
dir3_set = False
dir4_set = False
dir5_set = False

dir_set = [dir0_set, dir1_set, dir2_set, dir3_set, dir4_set, dir5_set]

def led_on():
    cmd = ('python ' + './display_1.py')
    sp = subprocess.Popen(cmd, shell=False, startupinfo=info)


def travel_wormhole():

    for dirName, subdirList, fileList in os.walk(wh_path):
        for fname in fileList:

            fullpath = os.path.join(wh_path_root, dirName, fname)

            if dir1_set is True:
                if fname.endswith(tuple(audext)):
                    print('-- move:', fullpath, '-->', aud_dest+fname)
                    led_on()
                    shutil.move(fullpath, aud_dest+fname)

            if dir2_set is True:
                if fname.endswith(tuple(imgext)):
                    print('-- move:', fullpath, '-->', img_dest+fname)
                    led_on()
                    shutil.move(fullpath, img_dest+fname)

            if dir3_set is True:
                if fname.endswith(tuple(txtext)):
                    print('-- move:', fullpath, '-->', txt_dest+fname)
                    led_on()
                    shutil.move(fullpath, txt_dest+fname)

            if dir4_set is True:
                if fname.endswith(tuple(vidext)):
                    print('-- move:', fullpath, '-->', vid_dest+fname)
                    led_on()
                    shutil.move(fullpath, vid_dest+fname)

            if dir5_set is True:
                if fname.endswith(tuple(exeext)):
                    print('-- move:', fullpath, '-->', exe_dest+fname)
                    led_on()
                    shutil.move(fullpath, exe_dest+fname)


def get_config():
    global wh_path
    global wh_path_root

    global aud_dest
    global img_dest
    global txt_dest
    global vid_dest
    global exe_dest

    global dir0_set
    global dir1_set
    global dir2_set
    global dir3_set
    global dir4_set
    global dir3_set

    global dir_set

    print('WORMHOLE CONFIGURATION')
    
    with open(config, 'r') as fo:
        for line in fo:
            line = line.strip()

            if line.startswith('wormhole: '):
                if line.endswith('\wormhole\\'):
                    wh_path = line.replace('wormhole: ', '')
                    wh_path = wh_path.strip()
                    wh_path_root = str(wh_path.split('\\')[0]+'\\')
                    
                    if os.path.exists(wh_path):
                        print('wormhole path     | ', wh_path)
                        dir0_set = True
                    else:
                        print('wormhole path     | ')
                        dir0_set = False
                    
            if line.startswith('audio: '):
                aud_dest = line.replace('audio: ', '')
                aud_dest = aud_dest.strip()
                aud_dest_root = str(aud_dest.split('\\')[0]+'\\')
                
                if os.path.exists(aud_dest):
                    print('audio destination | ', aud_dest)
                    dir1_set = True
                else:
                    print('audio destination | ')
                    dir1_set = False
                    
            if line.startswith('image: '):
                img_dest = line.replace('image: ', '')
                img_dest = img_dest.strip()
                img_dest_root = str(img_dest.split('\\')[0]+'\\')

                if os.path.exists(img_dest):
                    print('image destination | ', img_dest)
                    dir2_set = True
                else:
                    print('image destination | ')
                    dir2_set = False

            if line.startswith('documents: '):
                txt_dest = line.replace('documents: ', '')
                txt_dest = txt_dest.strip()
                txt_dest_root = str(txt_dest.split('\\')[0]+'\\')

                if os.path.exists(txt_dest):
                    print('doc destination   | ', txt_dest)
                    dir3_set = True
                else:
                    print('doc destination   | ')
                    dir3_set = False

            if line.startswith('video: '):
                vid_dest = line.replace('video: ', '')
                vid_dest = vid_dest.strip()
                vid_dest_root = str(vid_dest.split('\\')[0]+'\\')

                if os.path.exists(vid_dest):
                    print('video destination | ', vid_dest)
                    dir4_set = True
                else:
                    print('video destination | ')
                    dir4_set = False

            if line.startswith('program: '):
                exe_dest = line.replace('program: ', '')
                exe_dest = exe_dest.strip()
                exe_dest_root = str(exe_dest.split('\\')[0]+'\\')

                if os.path.exists(exe_dest):
                    print('exe destination   | ', exe_dest)
                    dir5_set = True
                else:
                    print('exe destination   | ')
                    dir5_set = False
        fo.close()
                    
    dir_set = [dir0_set, dir1_set, dir2_set, dir3_set, dir4_set, dir5_set]

while 1 == 1:
    os.system('cls')
    get_config()

    i = 0
    count_set_true = 0
    if dir0_set is True:
        
        for dir_sets in dir_set:
            if dir_set[i] == True:
                count_set_true += 1
            i += 1

        if count_set_true >= 1:
            print('\nPROCESSING')
            travel_wormhole()
            time.sleep(3)
        else:
            print('-- invalid configuration: destination path error')
            time.sleep(3)
        
    elif dir0_set is False:
        print('-- invalid configuration: wormhole path error')
        time.sleep(3)
