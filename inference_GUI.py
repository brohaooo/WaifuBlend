import sys
import os

# these modules are imported in inference function, to reduce reduce loading delays when starting the GUI
# import torch
# from torchvision import transforms
# from PIL import Image
# from model import *

from io import BytesIO

from GUI_ui import Ui_Form
from PySide6.QtCore import *   
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from threading import Thread

# ------------------ inference part ------------------
def inference(G_A2B, G_B2A, input_human_dir,input_girl_dir,random=False,env_list={}): 
    # obtain all environment variables from env_list
    Image = env_list['Image']
    test_transform = env_list['test_transform']
    latent_dim = env_list['latent_dim']
    num_styles = env_list['num_styles']
    torch = env_list['torch']
    transforms = env_list['transforms']
    # load anime girl image and get its content and style
    anime_girl_filepath = input_girl_dir
    anime_girl_pic = Image.open(anime_girl_filepath).convert('RGB')
    anime_girl_pic = test_transform(anime_girl_pic).unsqueeze(0)
    girl_content, girl_style = G_B2A.encode(anime_girl_pic)
    if random:
        girl_style = torch.randn([latent_dim])
    # load human face image and get its content and style
    human_face_filepath = input_human_dir
    human_face_pic = Image.open(human_face_filepath).convert('RGB')
    human_face_pic = test_transform(human_face_pic).unsqueeze(0)
    human_content, human_style = G_A2B.encode(human_face_pic) # human_content aka A_content
    # get the output image which is a fusion of human content and girl style
    human_2_girl_output = G_A2B.decode(human_content.repeat(num_styles,1,1,1), girl_style)
    raw_tensor_image = human_2_girl_output
    # squeece the image to 3 dimension
    raw_tensor_image = raw_tensor_image.squeeze(0)
    # clamp the image to [-1,1] and convert it to [0,1] 
    # (I don't know why, it is written in the training process)
    raw_tensor_image.clamp_(min=-1, max=1)
    raw_tensor_image.sub_(-1).div_(max(1 - (-1), 1e-5))
    # convert the image to PIL image
    final_output_image = transforms.ToPILImage()(raw_tensor_image)
    return final_output_image


class MyWidget(QWidget):
    # initialize GUI
    def __init__(self,G_A2B,G_B2A,base_dir):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.G_A2B = G_A2B
        self.G_B2A = G_B2A
        self.input_human_dir = None
        self.input_girl_dir = None
        # the default output path is at /output_dir/output_image.jpg
        self.output_dir = os.path.join(BASE_DIR,'output_dir/output_image.jpg')
        self.pil_image = None
        self.use_random = False
        # this dictionary is used to pass all environment variables to inference function
        self.env_list = {}
        self.ui.prompt_line.setText("initializing...")

    # bind model to GUI object
    def bind_model(self,G_A2B,G_B2A):
        self.G_A2B = G_A2B
        self.G_B2A = G_B2A

    # connect all buttons to their corresponding functions
    def connect_all_button(self):
        self.ui.start_blend.clicked.connect(self.start_blend_clicked)
        self.ui.upload_human.clicked.connect(self.open_human_file)
        self.ui.upload_girl.clicked.connect(self.open_girl_file)
        self.ui.save_image.clicked.connect(self.save_image)
        self.ui.random_gen.clicked.connect(self.start_random_clicked)

    # this function is called when user click the blend button
    @Slot()
    def start_blend_clicked(self):
        self.use_random = False
        self.ui.prompt_line.setText("generating image...")
        inference_thread = Thread(target=self.run_inference)
        inference_thread.start()

    # this function is called when user click the random generate button
    def start_random_clicked(self):
        self.use_random = True
        self.ui.prompt_line.setText("generating random style image...")
        inference_thread = Thread(target=self.run_inference)
        inference_thread.start()

    def run_inference(self):
        # if user did not upload both images(which caused inference failed), prompt user to upload both images
        # if user uploaded both images, start inference
        try:
            # pil_image is the output image of inference function
            self.pil_image = inference(self.G_A2B, self.G_B2A, input_human_dir=self.input_human_dir,input_girl_dir=self.input_girl_dir,random=self.use_random,env_list=self.env_list)
        except(ValueError, AttributeError):
            self.ui.prompt_line.setText("please upload both images")
            return
        # convert PIL image to QImage
        # first convert PIL image to byte array by defining a buffer
        buffer = BytesIO()
        self.pil_image.save(buffer, format="PNG")
        # from byte array create QImage
        qimage = QImage.fromData(buffer.getvalue())
        pixmap = QPixmap.fromImage(qimage)
        buffer.close()
        self.ui.output_pic.setPixmap(pixmap)
        self.ui.prompt_line.setText("complete!")

    def open_human_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "choose picture file", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        # if user choose a file path, show the image on the GUI
        if filePath:
            self.input_human_dir = filePath
            pixmap = QPixmap(filePath)
            if not pixmap.isNull():
                self.ui.human_pic.setPixmap(pixmap)
    
    def open_girl_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "choose picture file", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        # if user choose a file path, save the image to that path
        if filePath:
            self.input_girl_dir = filePath
            pixmap = QPixmap(filePath)
            if not pixmap.isNull():
                self.ui.girl_pic.setPixmap(pixmap)

    def save_image(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self, "save image", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        # if user choose a file path, save the image to that path
        if filePath:
            self.output_dir = filePath
            self.pil_image.save(filePath)
            self.ui.prompt_line.setText("save complete!")


def setup_model(window):
    import torch
    from torchvision import transforms
    from PIL import Image
    import model

    # define model parameters
    latent_dim = 8
    n_mlp = 5
    num_down = 3
    num_styles = 1
    # define model, which is used in inference 
    G_A2B = model.Generator(256, 4, latent_dim, n_mlp, channel_multiplier=1, lr_mlp=.01,n_res=1).eval()
    G_B2A = model.Generator(256, 4, latent_dim, n_mlp, channel_multiplier=1, lr_mlp=.01,n_res=1).eval()
    # try to load model, if not found, prompt user to place model.pt at /model_dir folder
    try:
        ckpt = torch.load(os.path.join(BASE_DIR,'model_dir/model.pt'), map_location=lambda storage, loc: storage)
    except FileNotFoundError:
        window.ui.prompt_line.setText("model not found, please place model.pt at /model_dir folder")
        return
    # load model G_A2B and G_B2A, which are human to anime girl and anime girl to human respectively
    G_A2B.load_state_dict(ckpt['G_A2B_ema'])
    G_B2A.load_state_dict(ckpt['G_B2A_ema'])
    # the pre-processing of the image, which is the same as in the training process
    test_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5), inplace=True)
    ])

    # bind model to GUI
    window.bind_model(G_A2B=G_A2B,G_B2A=G_B2A)
    # activate all buttons
    window.connect_all_button()
    # pass all environment variables to GUI, so that it can be used in inference function
    window.env_list['Image'] = Image
    window.env_list['test_transform'] = test_transform
    window.env_list['latent_dim'] = latent_dim
    window.env_list['num_styles'] = num_styles
    window.env_list['torch'] = torch
    window.env_list['transforms'] = transforms
    window.ui.prompt_line.setText("choose your photo and an anime girl photo...")





if __name__ == '__main__':
    # get the path of the current file
    BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
    # ------------------ GUI setup part ------------------
    # create GUI application
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))
    # initialize GUI without model
    window = MyWidget(G_A2B=None,G_B2A=None,base_dir=BASE_DIR)
    window.setWindowTitle("WaifuBlend")
    window.show()
    # ------------------ model setup part ------------------
    # create a thread to load model, so that the GUI can be used while loading
    model_thread = Thread(target=setup_model,args=(window,))
    model_thread.start()
    # --------------------------------------------------------
    # exit the GUI application when the window is closed
    sys.exit(app.exec())
