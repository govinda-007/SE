{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5c80e447-a8ed-41e2-ba18-11ac119d764c",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "attempted relative import with no known parent package",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[10], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msqlalchemy\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Column, Integer, String, Float\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01minfrastructure\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m SessionLocal, engine, Base\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mChargingStationModel\u001b[39;00m(Base):\n\u001b[1;32m      5\u001b[0m     __tablename__ \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcharging_stations\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "\u001b[0;31mImportError\u001b[0m: attempted relative import with no known parent package"
     ]
    }
   ],
   "source": [
    "from sqlalchemy import Column, Integer, String, Float\n",
    "from ..infrastructure import SessionLocal, engine, Base\n",
    "\n",
    "class ChargingStationModel(Base):\n",
    "    __tablename__ = \"charging_stations\"\n",
    "\n",
    "    station_id = Column(String, primary_key=True, index=True)\n",
    "    postal_code = Column(String, index=True)\n",
    "    latitude = Column(Float)\n",
    "    longitude = Column(Float)\n",
    "    street = Column(String)\n",
    "    district = Column(String)\n",
    "    federal_state = Column(String)\n",
    "    operator = Column(String)\n",
    "    power_charging_dev = Column(Integer)\n",
    "    type_charging_device = Column(String)\n",
    "    commission_date = Column(String)\n",
    "    type_charging_device=Column(String)\n",
    "    cs_status=Column(String)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac6471f2-88dc-4d93-93f3-af719f94b0ad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
